# Voice Automation Agent# Voice Automation Agent# Voice Automation Agent# Voice Automation Agent



A voice-powered scheduling assistant for booking appointments with natural language commands. Designed for healthcare, clinics, and office scheduling (assessment project).



## 🔗 GitHub RepositoryA voice-powered scheduling assistant for booking appointments with natural language commands. Designed for healthcare, clinics, and office scheduling (assessment project).



**[GitHub: voice-automation-agent](https://github.com/MOhamedAMrr30/voice-agent)**



## Features## FeaturesA voice-powered scheduling assistant for booking appointments with natural language commands (assessment project).A voice-powered scheduling assistant that lets you book appointments and manage your calendar using natural language voice commands.



- 🎤 Voice input for appointments

- 📅 List available clinic/hospital schedules

- 🔤 Natural language date/time parsing- Voice input for appointments

- ✅ Book appointments by voice

- 🔗 n8n webhook integration for automation- List available clinic/hospital schedules

- 🌐 Web-based interface with speech recognition

- Natural language date/time parsing## Quick Start## Features

## Quick Start

- Book appointments by voice

1. Install dependencies:

   ```bash- n8n webhook integration for automation

   pip install -r requirements.txt

   ```- Web-based interface with speech recognition



2. Start the server:1. Install dependencies:- 🎤 Voice input for natural appointment booking

   ```bash

   python app.py## Quick Start

   ```

   ```bash- 📅 Calendar synchronization with n8n automation

3. Open `http://localhost:5000` in your browser (Chrome recommended)

1. Install dependencies:

## Demo Usage

   ```bash   pip install -r requirements.txt- � Appointment search and query

### List Available Appointments

   pip install -r requirements.txt

Say: **"What appointments are available tomorrow?"**

- App will list all clinic slots for the next day   ```   ```- � Flexible date/time parsing



Say: **"Show me today's schedule"**

- App displays all appointments for today

2. Start the server:- 🌐 Web interface (no installation needed)

### Book an Appointment

   ```bash

Say: **"Book a doctor appointment tomorrow at 2 PM"**

- App parses the time and date   python app.py2. Start the server:

- Creates appointment in the system

- Confirms booking via n8n webhook   ```



Say: **"Schedule a checkup for Friday at 10 AM"**   ```bash## Quick Start

- Natural language parsing handles various date formats

- Supports: "today", "tomorrow", "next Monday", dates like "January 20th"3. Open `http://localhost:5000` in your browser (Chrome recommended)



## Sample Clinic Data   python app.py



The app comes pre-loaded with sample appointments:## Demo Usage



| Doctor | Specialty | Date | Time | Location |   ```### Setup

|--------|-----------|------|------|----------|

| Dr. Smith | Cardiology | Nov 14 | 09:00 | Room 101 |### List Available Appointments

| Dr. Johnson | Pediatrics | Nov 14 | 10:00 | Room 205 |

| Dr. Williams | Dentistry | Nov 14 | 14:00 | Dental Suite |Say: **"What appointments are available tomorrow?"**

| Dr. Brown | Orthopedics | Nov 15 | 11:00 | Room 301 |

| Dr. Davis | General Surgery | Nov 15 | 15:00 | OR 1 |- App will list all clinic slots for the next day



## API Endpoints3. Open `http://localhost:5000` in your browser1. Create a virtual environment:



- `GET /api/schedule?date=YYYY-MM-DD` — List appointments for a dateSay: **"Show me today's schedule"**

- `DELETE /api/schedule/<id>` — Cancel appointment

- `POST /api/search` — Search by natural language query- App displays all appointments for today   ```bash

- `POST /api/book` — Book from voice input



### Example: List Schedule

```bash### Book an Appointment4. Click **"Start Listening"** and say: "Book a meeting tomorrow at 2 PM"   python -m venv venv

curl http://localhost:5000/api/search \

  -H "Content-Type: application/json" \Say: **"Book a doctor appointment tomorrow at 2 PM"**

  -d '{"query": "what appointments tomorrow"}'

```- App parses the time and date   source venv/bin/activate  # On Windows: venv\Scripts\activate



Response:- Creates appointment in the system

```json

{- Confirms booking via n8n webhook## Features   ```

  "query": "what appointments tomorrow",

  "results": [

    {

      "id": 1,Say: **"Schedule a checkup for Friday at 10 AM"**

      "title": "Dr. Smith - Cardiology",

      "date": "2025-11-14",- Natural language parsing handles various date formats

      "time": "09:00",

      "location": "Room 101"- Supports: "today", "tomorrow", "next Monday", dates like "January 20th"- Voice input for appointments2. Install dependencies:

    }

  ],

  "count": 1

}## Sample Clinic Data- Natural language date/time parsing   ```bash

```



### Example: Book Appointment

```bashThe app comes pre-loaded with sample appointments:- Appointment search and management   pip install -r requirements.txt

curl http://localhost:5000/api/book \

  -H "Content-Type: application/json" \

  -d '{"text": "Book a checkup tomorrow at 2 PM"}'

```| Doctor | Specialty | Date | Time | Location |- n8n webhook integration for automation   ```



Response:|--------|-----------|------|------|----------|

```json

{| Dr. Smith | Cardiology | Nov 14 | 09:00 | Room 101 |- Web-based interface

  "message": "Appointment booked successfully",

  "appointment": {| Dr. Johnson | Pediatrics | Nov 14 | 10:00 | Room 205 |

    "id": 6,

    "title": "checkup",| Dr. Williams | Dentistry | Nov 14 | 14:00 | Dental Suite |3. Start the server:

    "date": "2025-11-14",

    "time": "14:00",| Dr. Brown | Orthopedics | Nov 15 | 11:00 | Room 301 |

    "created_at": "2025-11-13T..."

  }| Dr. Davis | General Surgery | Nov 15 | 15:00 | OR 1 |## API Endpoints   ```bash

}

```



## Files## API Endpoints   python app.py



- `app.py` — Flask backend with scheduling logic (277 lines)

- `index.html` — Web interface with voice recognition

- `n8n_integration.py` — n8n webhook handler- `GET /api/schedule?date=YYYY-MM-DD` — List appointments for a date- `GET /api/schedule?date=YYYY-MM-DD` — List appointments   ```

- `n8n_workflow.json` — n8n workflow definition

- `requirements.txt` — Python dependencies- `DELETE /api/schedule/<id>` — Cancel appointment



## Browser Support- `POST /api/search` — Search by natural language query- `DELETE /api/schedule/<id>` — Delete appointment



Works best in **Chrome/Chromium** (best voice recognition)- `POST /api/book` — Book from voice input

- Also supports: Edge, Safari

- Limited: Firefox- `POST /api/search` — Search by query4. Open your browser to `http://localhost:5000`



## Setup for Demonstration### Example: List Schedule



### Minimal Setup (Demo Only)```bash- `POST /api/book` — Book from voice text

```bash

# Install and runcurl http://localhost:5000/api/search \

pip install flask flask-cors

python app.py  -H "Content-Type: application/json" \### Using the App

# Open http://localhost:5000

```  -d '{"query": "what appointments tomorrow"}'



### Full Setup (with n8n integration)```## Files

Set environment variable for n8n webhook:

```bash

export N8N_WEBHOOK_URL="https://your-n8n-instance/webhook/ai-booking"

python app.pyResponse:1. Click **"Start Listening"** to begin recording

```

```json

## Technology Stack

{- `app.py` — Flask backend2. Say your appointment naturally:

- **Backend:** Python Flask + Flask-CORS

- **Frontend:** HTML5 + Web Speech API  "query": "what appointments tomorrow",

- **Automation:** n8n webhook integration

- **Database:** In-memory (demo) - can be replaced with PostgreSQL/MongoDB  "results": [- `index.html` — Web interface   - "Book a meeting tomorrow at 2 PM"

- **Calendar:** Google Calendar API (via n8n)

    {

## How It Works

      "id": 1,- `n8n_integration.py` — n8n webhook handler   - "Schedule a doctor appointment on January 20th at 10:30 AM"

1. **User speaks** a natural language command via the web interface

2. **Web Speech API** captures and transcribes the voice input      "title": "Dr. Smith - Cardiology",

3. **Flask backend** parses the command to extract:

   - Action (list/book)      "date": "2025-11-14",- `requirements.txt` — Dependencies3. Click **"Stop & Process"** to submit

   - Date/time (today, tomorrow, specific dates)

   - Duration and other details      "time": "09:00",

4. **Appointment system** stores/retrieves from in-memory database

5. **n8n webhook** sends booking confirmation for external processing      "location": "Room 101"4. Your appointment is created and sent to n8n for processing

6. **Response** is sent back with confirmation or list of appointments

    }

### Voice Parsing Examples

  ],## Notes

- **Input:** "What appointments do I have tomorrow?"

  - **Parsed:** action=search, date=tomorrow  "count": 1

  - **Result:** List of appointments for next day

}## API Endpoints

- **Input:** "Book a cardiology appointment Friday at 2 PM"

  - **Parsed:** action=book, title=cardiology, date=Friday, time=14:00```

  - **Result:** Appointment created, confirmation sent

- Data stored in memory (demo only)

## API Request Examples

### Example: Book Appointment

### List Today's Appointments

```bash```bash- Voice recognition works best in Chrome### GET /api/schedule

curl http://localhost:5000/api/schedule?date=2025-11-13

```curl http://localhost:5000/api/book \



### Search by Natural Language  -H "Content-Type: application/json" \- n8n integration requires webhook configurationRetrieve appointments

```bash

curl -X POST http://localhost:5000/api/search \  -d '{"text": "Book a checkup tomorrow at 2 PM"}'

  -H "Content-Type: application/json" \

  -d '{"query": "doctor appointments next week"}'``````bash

```

GET /api/schedule?date=2025-01-15

### Book New Appointment

```bashResponse:```

curl -X POST http://localhost:5000/api/book \

  -H "Content-Type: application/json" \```json

  -d '{"text": "Schedule a meeting tomorrow at 10 AM"}'

```{### POST /api/schedule



### Cancel Appointment  "message": "Appointment booked successfully",Create an appointment

```bash

curl -X DELETE http://localhost:5000/api/schedule/1  "appointment": {```bash

```

    "id": 6,POST /api/schedule

## Features in Detail

    "title": "checkup",{

### Natural Language Processing

- Handles flexible date formats: "today", "tomorrow", "next Monday", "January 20th"    "date": "2025-11-14",  "title": "Meeting",

- Extracts time: "2 PM", "14:00", "2 o'clock"

- Supports appointment types: "doctor", "checkup", "meeting", "consultation"    "time": "14:00",  "date": "2025-01-15",

- Parses duration: "1 hour", "30 minutes" (optional)

    "created_at": "2025-11-13T..."  "time": "14:00",

### Appointment Management

- Create appointments from voice input  }  "duration": 60

- List appointments by date range

- Delete/cancel appointments}}

- View appointment details (doctor, time, location, participants)

``````

### n8n Integration

- Sends appointment data via webhook

- Receives confirmation or conflict alerts

- Processes calendar conflicts## Files### POST /api/search

- Suggests alternative times if needed

Search appointments

## Notes

- `app.py` — Flask backend with scheduling logic```bash

- Data stored in memory (resets on restart)

- Voice recognition requires microphone and modern browser- `index.html` — Web interface with voice recognitionPOST /api/search

- n8n integration requires webhook configuration

- Sample data includes 5 clinic appointments for demo purposes- `n8n_integration.py` — n8n webhook handler{

- Best used with Chrome/Chromium for optimal voice recognition

- `n8n_workflow.json` — n8n workflow definition  "query": "What's on my calendar today?"

## Assessment Context

- `requirements.txt` — Python dependencies}

This is a demonstration project showcasing:

- Voice-based appointment scheduling```

- Natural language parsing

- RESTful API design## Browser Support

- Frontend-backend integration

- Workflow automation with n8n### POST /api/book

- Professional code standards

Works best in **Chrome/Chromium** (best voice recognition)Book from voice input

Perfect for: Hospital scheduling, clinic bookings, office appointments, demo presentations

- Also supports: Edge, Safari```bash

## Getting Started

- Limited: FirefoxPOST /api/book

1. **Clone the repository:**

   ```bash{

   git clone https://github.com/MOhamedAMrr30/voice-agent.git

   cd voice-agent## Setup for Demonstration  "text": "Book a meeting tomorrow at 2 PM"

   ```

}

2. **Install dependencies:**

   ```bash### Minimal Setup (Demo Only)```

   pip install -r requirements.txt

   ``````bash



3. **Run the application:**# Install and run## n8n Integration

   ```bash

   python app.pypip install flask flask-cors

   ```

python app.pyThe app sends appointment data to n8n via webhook for:

4. **Open in browser:**

   ```# Open http://localhost:5000- Checking calendar availability

   http://localhost:5000

   ``````- Detecting scheduling conflicts



5. **Test voice commands:**- Creating Google Calendar events

   - Click "Start Listening"

   - Say: "What appointments are available tomorrow?"### Full Setup (with n8n integration)- Suggesting alternative times if conflicts exist

   - Say: "Book an appointment for tomorrow at 2 PM"

Set environment variable for n8n webhook:

## Delivery Documentation

```bash### Setup n8n

See additional documentation for assessment submission:

- **SUBMISSION_CHECKLIST.md** — Assessment requirements and demo scriptexport N8N_WEBHOOK_URL="https://your-n8n-instance/webhook/ai-booking"

- **DELIVERY_GUIDE.md** — Step-by-step GitHub and recording setup

- **PROJECT_STATUS.md** — Complete project status summarypython app.py1. Create an n8n workflow with:



---```   - Webhook node (receives appointment data)



**Repository:** [MOhamedAMrr30/voice-agent](https://github.com/MOhamedAMrr30/voice-agent)   - Google Calendar nodes (list and create events)



**Status:** ✅ Complete and ready for assessment## Delivery Requirements   - IF node (check for conflicts)


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
#   v o i c e - a g e n t 
 
 #   v o i c e - a g e n t  
 