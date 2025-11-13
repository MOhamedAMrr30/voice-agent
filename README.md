# Voice Automation Agent# Voice Automation Agent



A voice-powered scheduling assistant for booking appointments with natural language commands (assessment project).A voice-powered scheduling assistant that lets you book appointments and manage your calendar using natural language voice commands.



## Quick Start## Features



1. Install dependencies:- 🎤 Voice input for natural appointment booking

   ```bash- 📅 Calendar synchronization with n8n automation

   pip install -r requirements.txt- � Appointment search and query

   ```- � Flexible date/time parsing

- 🌐 Web interface (no installation needed)

2. Start the server:

   ```bash## Quick Start

   python app.py

   ```### Setup



3. Open `http://localhost:5000` in your browser1. Create a virtual environment:

   ```bash

4. Click **"Start Listening"** and say: "Book a meeting tomorrow at 2 PM"   python -m venv venv

   source venv/bin/activate  # On Windows: venv\Scripts\activate

## Features   ```



- Voice input for appointments2. Install dependencies:

- Natural language date/time parsing   ```bash

- Appointment search and management   pip install -r requirements.txt

- n8n webhook integration for automation   ```

- Web-based interface

3. Start the server:

## API Endpoints   ```bash

   python app.py

- `GET /api/schedule?date=YYYY-MM-DD` — List appointments   ```

- `DELETE /api/schedule/<id>` — Delete appointment

- `POST /api/search` — Search by query4. Open your browser to `http://localhost:5000`

- `POST /api/book` — Book from voice text

### Using the App

## Files

1. Click **"Start Listening"** to begin recording

- `app.py` — Flask backend2. Say your appointment naturally:

- `index.html` — Web interface   - "Book a meeting tomorrow at 2 PM"

- `n8n_integration.py` — n8n webhook handler   - "Schedule a doctor appointment on January 20th at 10:30 AM"

- `requirements.txt` — Dependencies3. Click **"Stop & Process"** to submit

4. Your appointment is created and sent to n8n for processing

## Notes

## API Endpoints

- Data stored in memory (demo only)

- Voice recognition works best in Chrome### GET /api/schedule

- n8n integration requires webhook configurationRetrieve appointments

```bash
GET /api/schedule?date=2025-01-15
```

### POST /api/schedule
Create an appointment
```bash
POST /api/schedule
{
  "title": "Meeting",
  "date": "2025-01-15",
  "time": "14:00",
  "duration": 60
}
```

### POST /api/search
Search appointments
```bash
POST /api/search
{
  "query": "What's on my calendar today?"
}
```

### POST /api/book
Book from voice input
```bash
POST /api/book
{
  "text": "Book a meeting tomorrow at 2 PM"
}
```

## n8n Integration

The app sends appointment data to n8n via webhook for:
- Checking calendar availability
- Detecting scheduling conflicts
- Creating Google Calendar events
- Suggesting alternative times if conflicts exist

### Setup n8n

1. Create an n8n workflow with:
   - Webhook node (receives appointment data)
   - Google Calendar nodes (list and create events)
   - IF node (check for conflicts)
   - Function node (generate alternatives)

2. Set your webhook URL:
   ```bash
   export N8N_WEBHOOK_URL="https://your-instance.n8n.cloud/webhook/ai-booking"
   ```

3. Import `n8n_workflow_cleaned.json` as your workflow

## Browser Support

- ✅ Chrome/Chromium (recommended)
- ✅ Edge
- ✅ Safari
- ⚠️ Firefox (limited speech recognition)

## Project Structure

```
voice-agent/
├── app.py                      # Flask backend
├── index.html                  # Web interface
├── n8n_integration.py          # n8n webhook handler
├── n8n_workflow_cleaned.json   # n8n workflow
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## Notes

- Appointments are stored in memory (resets on restart)
- For production, use a database
- Voice recognition depends on microphone quality
- Google Calendar sync requires n8n configuration

