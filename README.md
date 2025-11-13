# Voice Automation Agent# Voice Automation Agent# Voice Automation Agent



A voice-powered scheduling assistant for booking appointments with natural language commands. Designed for healthcare, clinics, and office scheduling (assessment project).



## FeaturesA voice-powered scheduling assistant for booking appointments with natural language commands (assessment project).A voice-powered scheduling assistant that lets you book appointments and manage your calendar using natural language voice commands.



- Voice input for appointments

- List available clinic/hospital schedules

- Natural language date/time parsing## Quick Start## Features

- Book appointments by voice

- n8n webhook integration for automation

- Web-based interface with speech recognition

1. Install dependencies:- 🎤 Voice input for natural appointment booking

## Quick Start

   ```bash- 📅 Calendar synchronization with n8n automation

1. Install dependencies:

   ```bash   pip install -r requirements.txt- � Appointment search and query

   pip install -r requirements.txt

   ```   ```- � Flexible date/time parsing



2. Start the server:- 🌐 Web interface (no installation needed)

   ```bash

   python app.py2. Start the server:

   ```

   ```bash## Quick Start

3. Open `http://localhost:5000` in your browser (Chrome recommended)

   python app.py

## Demo Usage

   ```### Setup

### List Available Appointments

Say: **"What appointments are available tomorrow?"**

- App will list all clinic slots for the next day

3. Open `http://localhost:5000` in your browser1. Create a virtual environment:

Say: **"Show me today's schedule"**

- App displays all appointments for today   ```bash



### Book an Appointment4. Click **"Start Listening"** and say: "Book a meeting tomorrow at 2 PM"   python -m venv venv

Say: **"Book a doctor appointment tomorrow at 2 PM"**

- App parses the time and date   source venv/bin/activate  # On Windows: venv\Scripts\activate

- Creates appointment in the system

- Confirms booking via n8n webhook## Features   ```



Say: **"Schedule a checkup for Friday at 10 AM"**

- Natural language parsing handles various date formats

- Supports: "today", "tomorrow", "next Monday", dates like "January 20th"- Voice input for appointments2. Install dependencies:



## Sample Clinic Data- Natural language date/time parsing   ```bash



The app comes pre-loaded with sample appointments:- Appointment search and management   pip install -r requirements.txt



| Doctor | Specialty | Date | Time | Location |- n8n webhook integration for automation   ```

|--------|-----------|------|------|----------|

| Dr. Smith | Cardiology | Nov 14 | 09:00 | Room 101 |- Web-based interface

| Dr. Johnson | Pediatrics | Nov 14 | 10:00 | Room 205 |

| Dr. Williams | Dentistry | Nov 14 | 14:00 | Dental Suite |3. Start the server:

| Dr. Brown | Orthopedics | Nov 15 | 11:00 | Room 301 |

| Dr. Davis | General Surgery | Nov 15 | 15:00 | OR 1 |## API Endpoints   ```bash



## API Endpoints   python app.py



- `GET /api/schedule?date=YYYY-MM-DD` — List appointments for a date- `GET /api/schedule?date=YYYY-MM-DD` — List appointments   ```

- `DELETE /api/schedule/<id>` — Cancel appointment

- `POST /api/search` — Search by natural language query- `DELETE /api/schedule/<id>` — Delete appointment

- `POST /api/book` — Book from voice input

- `POST /api/search` — Search by query4. Open your browser to `http://localhost:5000`

### Example: List Schedule

```bash- `POST /api/book` — Book from voice text

curl http://localhost:5000/api/search \

  -H "Content-Type: application/json" \### Using the App

  -d '{"query": "what appointments tomorrow"}'

```## Files



Response:1. Click **"Start Listening"** to begin recording

```json

{- `app.py` — Flask backend2. Say your appointment naturally:

  "query": "what appointments tomorrow",

  "results": [- `index.html` — Web interface   - "Book a meeting tomorrow at 2 PM"

    {

      "id": 1,- `n8n_integration.py` — n8n webhook handler   - "Schedule a doctor appointment on January 20th at 10:30 AM"

      "title": "Dr. Smith - Cardiology",

      "date": "2025-11-14",- `requirements.txt` — Dependencies3. Click **"Stop & Process"** to submit

      "time": "09:00",

      "location": "Room 101"4. Your appointment is created and sent to n8n for processing

    }

  ],## Notes

  "count": 1

}## API Endpoints

```

- Data stored in memory (demo only)

### Example: Book Appointment

```bash- Voice recognition works best in Chrome### GET /api/schedule

curl http://localhost:5000/api/book \

  -H "Content-Type: application/json" \- n8n integration requires webhook configurationRetrieve appointments

  -d '{"text": "Book a checkup tomorrow at 2 PM"}'

``````bash

GET /api/schedule?date=2025-01-15

Response:```

```json

{### POST /api/schedule

  "message": "Appointment booked successfully",Create an appointment

  "appointment": {```bash

    "id": 6,POST /api/schedule

    "title": "checkup",{

    "date": "2025-11-14",  "title": "Meeting",

    "time": "14:00",  "date": "2025-01-15",

    "created_at": "2025-11-13T..."  "time": "14:00",

  }  "duration": 60

}}

``````



## Files### POST /api/search

Search appointments

- `app.py` — Flask backend with scheduling logic```bash

- `index.html` — Web interface with voice recognitionPOST /api/search

- `n8n_integration.py` — n8n webhook handler{

- `n8n_workflow.json` — n8n workflow definition  "query": "What's on my calendar today?"

- `requirements.txt` — Python dependencies}

```

## Browser Support

### POST /api/book

Works best in **Chrome/Chromium** (best voice recognition)Book from voice input

- Also supports: Edge, Safari```bash

- Limited: FirefoxPOST /api/book

{

## Setup for Demonstration  "text": "Book a meeting tomorrow at 2 PM"

}

### Minimal Setup (Demo Only)```

```bash

# Install and run## n8n Integration

pip install flask flask-cors

python app.pyThe app sends appointment data to n8n via webhook for:

# Open http://localhost:5000- Checking calendar availability

```- Detecting scheduling conflicts

- Creating Google Calendar events

### Full Setup (with n8n integration)- Suggesting alternative times if conflicts exist

Set environment variable for n8n webhook:

```bash### Setup n8n

export N8N_WEBHOOK_URL="https://your-n8n-instance/webhook/ai-booking"

python app.py1. Create an n8n workflow with:

```   - Webhook node (receives appointment data)

   - Google Calendar nodes (list and create events)

## Delivery Requirements   - IF node (check for conflicts)

   - Function node (generate alternatives)

### 1. GitHub Repository

[Your GitHub Repository Link](https://github.com/yourusername/voice-automation-agent)2. Set your webhook URL:

   ```bash

To push this locally to GitHub:   export N8N_WEBHOOK_URL="https://your-instance.n8n.cloud/webhook/ai-booking"

```bash   ```

# Create a new repo on GitHub, then:

git remote add origin https://github.com/yourusername/voice-automation-agent.git3. Import `n8n_workflow_cleaned.json` as your workflow

git branch -M main

git push -u origin main## Browser Support

```

- ✅ Chrome/Chromium (recommended)

### 2. Screen Recording (5 min max)- ✅ Edge

- ✅ Safari

**Demo Script:**- ⚠️ Firefox (limited speech recognition)

1. **Intro (30s)** - Show the app interface, explain it's a voice-powered scheduling assistant

2. **List Schedules (1m)** - Voice command: "What appointments are available tomorrow?" → Show results## Project Structure

3. **Book Appointment (1.5m)** - Voice command: "Book a doctor appointment tomorrow at 2 PM" → Confirm booking

4. **Verify (1m)** - Show the appointment was added to the schedule```

voice-agent/

**Recording Steps:**├── app.py                      # Flask backend

- Open app in browser: http://localhost:5000├── index.html                  # Web interface

- Start screen recording (Windows: Win+G, Mac: Cmd+Shift+5)├── n8n_integration.py          # n8n webhook handler

- Use browser's voice input or say commands clearly├── n8n_workflow_cleaned.json   # n8n workflow

- Show backend response/confirmation├── requirements.txt            # Dependencies

- Stop recording when done└── README.md                   # This file

```

**File Format:** MP4 or WebM (< 100MB)

## Notes

## Notes

- Appointments are stored in memory (resets on restart)

- Data stored in memory (resets on restart)- For production, use a database

- Voice recognition requires microphone and modern browser- Voice recognition depends on microphone quality

- n8n integration requires webhook configuration- Google Calendar sync requires n8n configuration

- Sample data includes 5 clinic appointments for demo purposes


## Assessment Context

This is a demonstration project showcasing:
- Voice-based appointment scheduling
- Natural language parsing
- RESTful API design
- Frontend-backend integration
- Workflow automation with n8n

Perfect for: Hospital scheduling, clinic bookings, office appointments, demo presentations
#   v o i c e - a g e n t  
 