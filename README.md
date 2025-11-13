# 🗣️ Voice Automation Agent

A **voice-powered scheduling assistant** for booking appointments with natural language commands.  
Designed for healthcare, clinics, and office scheduling (assessment project).

---

## 🔗 GitHub Repository
**[MOhamedAMrr30/voice-agent](https://github.com/MOhamedAMrr30/voice-agent)**

---

## ✨ Features

- 🎤 Voice input for natural appointment booking  
- 📅 List available clinic or hospital schedules  
- 🔤 Natural language date/time parsing (e.g., “next Monday at 3 PM”)  
- ✅ Book appointments and confirm via n8n webhook integration  
- 🔗 Automated Google Calendar sync  
- 🌐 Web-based interface using Web Speech API  
- ⚙️ Flask backend with n8n automation integration  

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt


🚀 Quick Start

Clone the repo:

git clone https://github.com/MOhamedAMrr30/voice-agent.git
cd voice-agent


Install dependencies:

pip install -r requirements.txt


Run the server:

python app.py


Open in your browser:

http://localhost:5000


Try voice commands:

“What appointments are available tomorrow?”

“Book a doctor appointment tomorrow at 2 PM.”

🧠 Demo Usage
🔍 List Appointments

Say: “What appointments are available tomorrow?”
➡️ The app lists all available clinic slots for the next day.

🩺 Book Appointment

Say: “Book a checkup for Friday at 10 AM.”
➡️ The app parses, books, and confirms via n8n webhook.


⚙️ n8n Integration

Create an n8n workflow with:

Webhook node (receive appointment data)

Google Calendar nodes (list + create events)

IF node (check conflicts)

Function node (suggest alternative times)

Set your webhook environment variable:

export N8N_WEBHOOK_URL="https://your-n8n-instance/webhook/ai-booking"
python app.py


Example webhook payload:

{
  "clientName": "Sara Ahmed",
  "clientEmail": "sara@example.com",
  "phone": "+201234567890",
  "start": "2025-11-20T15:00:00",
  "end": "2025-11-20T15:30:00",
  "timezone": "Africa/Cairo",
  "subject": "Consultation",
  "calendarId": "primary"
}


✅ n8n checks Google Calendar availability, books if free, and sends confirmation or alternatives if a conflict exists.
