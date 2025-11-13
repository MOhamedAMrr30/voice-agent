from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import os
import re

try:
    import dateparser
    DATEPARSER_AVAILABLE = True
except ImportError:
    DATEPARSER_AVAILABLE = False

USE_N8N_FOR_CALENDAR = os.getenv('USE_N8N_FOR_CALENDAR', 'true').lower() == 'true'
ENABLE_N8N = os.getenv('ENABLE_N8N', 'true').lower() == 'true'
N8N_ENABLED = ENABLE_N8N or USE_N8N_FOR_CALENDAR

# Prepare defaults so other code can reference these safely
N8N_AVAILABLE = False
n8n_create_calendar_event = None
if N8N_ENABLED:
    try:
        from n8n_integration import n8n_create_calendar_event
        N8N_AVAILABLE = True
        print("[INFO] n8n integration enabled")
    except ImportError:
        N8N_AVAILABLE = False
        print("[WARNING] n8n integration not available. Install: pip install requests")
        if USE_N8N_FOR_CALENDAR:
            print("[WARNING] n8n is required for calendar integration!")

app = Flask(__name__)
CORS(app)

appointments = []

@app.route('/')
def index():
    return "Voice Automation Agent API"

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    """Get appointments, optionally filtered by date"""
    date_filter = request.args.get('date')
    
    if date_filter:
        filtered = [a for a in appointments if a.get('date') == date_filter]
        return jsonify({"schedule": filtered, "count": len(filtered)})
    
    return jsonify({"schedule": appointments, "count": len(appointments)})

@app.route('/api/schedule/<int:appointment_id>', methods=['DELETE'])
def delete_schedule(appointment_id):
    """Delete an appointment"""
    global appointments
    appointments = [a for a in appointments if a.get('id') != appointment_id]
    return jsonify({"message": "Appointment deleted successfully"})

@app.route('/api/search', methods=['POST'])
def query_schedule():
    """Search appointments with natural language"""
    data = request.json
    query = data.get('query', '').lower()
    
    
    results = []
    
    if 'after tomorrow' in query or 'day after tomorrow' in query:
        day_after_tomorrow_str = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        results = [a for a in appointments if a.get('date') == day_after_tomorrow_str]
    elif 'today' in query:
        today_str = datetime.now().strftime('%Y-%m-%d')
        results = [a for a in appointments if a.get('date') == today_str]
    elif 'tomorrow' in query:
        tomorrow_str = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        results = [a for a in appointments if a.get('date') == tomorrow_str]
    elif 'this week' in query:
        today = datetime.now()
        week_end = today + timedelta(days=7)
        results = [a for a in appointments if 
                   a.get('date') and today.strftime('%Y-%m-%d') <= a.get('date') <= week_end.strftime('%Y-%m-%d')]
    else:
        results = appointments
    
    return jsonify({
        "query": query,
        "results": results,
        "count": len(results)
    })

def parse_voice_command(text):
    """Parse voice command to extract appointment details."""
    time_patterns = [
        r'(\d{1,2})\s*(?:am|pm)',
        r'(\d{1,2}):(\d{2})\s*(?:am|pm)?',
        r'at\s+(\d{1,2})\s*(?:am|pm)',
        r'at\s+(\d{1,2}):(\d{2})\s*(?:am|pm)?',
    ]
    
    text_lower = text.lower()
    title = "New Appointment"
    
    prefixes = ['book', 'schedule', 'create', 'add', 'set up', 'make']
    for prefix in prefixes:
        if text_lower.startswith(prefix):
            text_lower = text_lower[len(prefix):].strip()
            break
    
    time_str = None
    time_match = None
    for pattern in time_patterns:
        time_match = re.search(pattern, text_lower, re.IGNORECASE)
        if time_match:
            hours = int(time_match.group(1))
            minutes = int(time_match.group(2)) if len(time_match.groups()) > 1 and time_match.group(2) else 0
            
            if 'pm' in time_match.group(0).lower() and hours != 12:
                hours += 12
            elif 'am' in time_match.group(0).lower() and hours == 12:
                hours = 0
            
            time_str = f"{hours:02d}:{minutes:02d}"
            break
    
    parsed_date = None
    if DATEPARSER_AVAILABLE:
        parsed_date = dateparser.parse(text, settings={'RELATIVE_BASE': datetime.now()})
    
    # Fallback to keyword matching
    if not parsed_date:
        if 'after tomorrow' in text_lower or 'day after tomorrow' in text_lower:
            parsed_date = datetime.now() + timedelta(days=2)
        elif 'today' in text_lower:
            parsed_date = datetime.now()
        elif 'tomorrow' in text_lower:
            parsed_date = datetime.now() + timedelta(days=1)
        elif 'next week' in text_lower:
            parsed_date = datetime.now() + timedelta(days=7)
        elif 'day after' in text_lower:
            parsed_date = datetime.now() + timedelta(days=2)
        else:
            date_pattern = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
            date_match = re.search(date_pattern, text)
            if date_match:
                try:
                    month, day, year = date_match.groups()
                    year = int(year) if len(year) == 4 else int('20' + year)
                    parsed_date = datetime(year, int(month), int(day))
                except:
                    parsed_date = datetime.now()
            else:
                parsed_date = datetime.now()
    
    # Extract title (remove date/time keywords and common words)
    title_text = text
    if time_match:
        title_text = title_text[:time_match.start()] + title_text[time_match.end():]
    
    # Remove date keywords
    date_keywords = ['today', 'tomorrow', 'next week', 'on', 'at']
    for keyword in date_keywords:
        title_text = re.sub(rf'\b{keyword}\b', '', title_text, flags=re.IGNORECASE)
    
    # Clean up title
    title_text = re.sub(r'\s+', ' ', title_text).strip()
    if title_text and len(title_text) > 3:
        title_text = re.sub(r'\b(appointment|meeting|event)\b$', '', title_text, flags=re.IGNORECASE).strip()
        if title_text:
            title = title_text
    
    date_str = parsed_date.strftime('%Y-%m-%d')
    if not time_str:
        time_str = parsed_date.strftime('%H:%M')
        if 'today' not in text_lower and 'tomorrow' not in text_lower:
            time_str = '10:00'
    
    return {
        "title": title,
        "date": date_str,
        "time": time_str,
        "duration": 60 
    }

@app.route('/api/book', methods=['POST'])
def book_appointment():
    """Book an appointment from voice input with improved parsing"""
    data = request.json
    text = data.get('text', '') or data.get('command', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Parse voice command
    if data.get('title') and data.get('date') and data.get('time'):
        # Already parsed on frontend
        appointment_data = {
            "title": data.get('title'),
            "date": data.get('date'),
            "time": data.get('time'),
            "duration": data.get('duration', 60)
        }
    else:
        appointment_data = parse_voice_command(text)
    
    new_id = max([a.get('id', 0) for a in appointments], default=0) + 1
    appointment = {
        "id": new_id,
        **appointment_data,
        "participants": data.get('participants', []),
        "created_at": datetime.now().isoformat(),
        "source": "voice_agent"
    }
    
    appointments.append(appointment)
    
    calendar_sync_result = None
    calendar_error = None
    
    if USE_N8N_FOR_CALENDAR and N8N_AVAILABLE:
        try:
            print(f"[DEBUG] Sending appointment to n8n workflow: {appointment.get('title')}")
            calendar_sync_result = n8n_create_calendar_event(appointment)
            print(f"[DEBUG] n8n workflow result: {calendar_sync_result}")
            
            if calendar_sync_result:
                if calendar_sync_result.get('success'):
                    appointment['calendar_event_id'] = calendar_sync_result.get('event_id')
                    appointment['calendar_link'] = calendar_sync_result.get('html_link')
                    print(f"[INFO] Google Calendar event created via n8n workflow")
                    if calendar_sync_result.get('html_link'):
                        print(f"[INFO] Calendar link: {calendar_sync_result.get('html_link')}")
                elif calendar_sync_result.get('conflict'):
                    print(f"[INFO] Time conflict detected: {calendar_sync_result.get('message')}")
                    if calendar_sync_result.get('alternatives'):
                        print(f"[INFO] Alternatives: {calendar_sync_result.get('alternatives')}")
                else:
                    error_msg = calendar_sync_result.get('error', 'Unknown error')
                    print(f"[ERROR] n8n workflow error: {error_msg}")
        except Exception as e:
            calendar_error = str(e)
            print(f"[ERROR] n8n workflow exception: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("[WARNING] No calendar integration available (n8n not configured)")
    
    response = {
        "message": "Appointment booked successfully",
        "appointment": appointment
    }
    
    if calendar_sync_result:
        response["calendar_sync"] = calendar_sync_result
        
        if calendar_sync_result.get('success'):
            response["message"] += " and added to Google Calendar"
            html_link = calendar_sync_result.get('html_link')
            if html_link:
                response["calendar_link"] = html_link
                print(f"[INFO] Calendar link added to response: {html_link}")
        
        elif calendar_sync_result.get('conflict'):
            response["conflict"] = True
            response["message"] = calendar_sync_result.get('message', 'Time conflict detected')
            response["alternatives"] = calendar_sync_result.get('alternatives', [])
            response["conflicting_events"] = calendar_sync_result.get('conflicting_events', [])
            print(f"[INFO] Conflict response sent to frontend")
        
        else:
            error_msg = calendar_sync_result.get('error', 'Unknown error')
            response["calendar_error"] = error_msg
            response["message"] += " (but failed to sync with Google Calendar)"
            print(f"[ERROR] Calendar sync failed: {error_msg}")
    
    elif calendar_error:
        response["calendar_error"] = calendar_error
        response["message"] += " (but failed to sync with Google Calendar)"
        print(f"[ERROR] Calendar error: {calendar_error}")
    
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)

