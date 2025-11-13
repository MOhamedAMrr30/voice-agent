# Delivery Setup Guide

This guide walks you through the final two delivery requirements for the voice automation agent assessment.

## Task 1: Create GitHub Repository

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Fill in:
   - Repository name: `voice-automation-agent` (or similar)
   - Description: "Voice-powered appointment scheduling system with n8n integration"
   - Choose: Public (for easy sharing)
   - DO NOT initialize with README (we already have one)
3. Click **Create repository**

### Step 2: Push Code to GitHub

Copy this command and run it in your terminal (Windows PowerShell):

```powershell
cd "C:\Users\DELL E5570 i5\Desktop\voice agent"
git remote add origin https://github.com/YOUR_USERNAME/voice-automation-agent.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username**

### Step 3: Verify Upload
- Visit your GitHub repo URL: `https://github.com/YOUR_USERNAME/voice-automation-agent`
- Confirm you see:
  - ✅ app.py
  - ✅ index.html
  - ✅ n8n_integration.py
  - ✅ n8n_workflow.json
  - ✅ requirements.txt
  - ✅ README.md

### Step 4: Update Local README
Edit your local `README.md` and replace:
```
[Your GitHub Repository Link](https://github.com/yourusername/voice-automation-agent)
```

With:
```
[GitHub Repository: voice-automation-agent](https://github.com/YOUR_USERNAME/voice-automation-agent)
```

Commit this change:
```powershell
git add README.md
git commit -m "docs: Add GitHub repository link"
git push
```

**Your GitHub link is ready to submit!**

---

## Task 2: Record 5-Minute Screen Demo

### Demo Flow (Total: ~5 minutes)

#### 1. Intro (30 seconds)
- Say: "This is a voice-powered clinic scheduling system. I can list appointments and book new ones using natural language."
- Show the Flask app running at http://localhost:5000
- Show the interface with "Start Listening" button visible

#### 2. List Appointments (1 minute)
- Click **"Start Listening"**
- Say: **"What appointments are available tomorrow?"**
- Wait for response
- Show the list of results displayed
- Example expected result:
  ```
  Dr. Smith - Cardiology @ 09:00 in Room 101
  Dr. Johnson - Pediatrics @ 10:00 in Room 205
  Dr. Williams - Dentistry @ 14:00 in Dental Suite
  ```

#### 3. Book Appointment (1.5 minutes)
- Click **"Start Listening"** again
- Say: **"Book an appointment for tomorrow at 2 PM with a doctor"**
- Wait for booking confirmation
- Show the success message
- Optionally, query again to verify the appointment was added

#### 4. Verify & Summary (1 minute)
- Query one more time to confirm the new appointment is in the schedule
- End with: "That's how you can book and manage appointments using voice commands."

### Recording Instructions

#### Option A: Windows GameBar (Built-in, Easiest)
1. Open the Flask app browser window
2. Press **Win + G** to open GameBar
3. Click **Capture** → **Start recording**
4. Perform the demo steps above
5. Press **Win + G** again → Stop recording
6. Recording saved to: `C:\Users\[YourUsername]\Videos\Captures`

#### Option B: OBS Studio (Free, Professional)
1. Download: https://obsproject.com
2. Add "Window Capture" source → select Chrome/Edge with Flask app
3. Click **Start Recording**
4. Perform demo steps
5. Click **Stop Recording**
6. Recording saved to default OBS folder

#### Option C: Bandicam (Lightweight)
1. Download free version: https://www.bandicam.com
2. Select region to capture (browser window)
3. Click **REC** to start
4. Perform demo
5. Click **REC** again to stop

### Recording Checklist
- ✅ Microphone audio is clear
- ✅ Browser window is visible and readable
- ✅ Voice commands are audible (not whispered)
- ✅ Response messages/confirmations are visible
- ✅ Total duration: 3-5 minutes (max 5 minutes)
- ✅ File format: MP4 or WebM
- ✅ File size: < 100 MB

### Save Your Recording

Once recorded, save the file as:
```
voice-agent-demo.mp4
```

Or upload to a cloud storage and get a sharable link:
- Google Drive
- OneDrive
- YouTube (unlisted)
- Dropbox

---

## Submission Checklist

Before submitting your assessment, verify you have:

- [ ] **GitHub Repository Link**
  - Repository created at GitHub.com
  - Code pushed successfully
  - README includes link
  - Repo is public and accessible

- [ ] **Screen Recording (5 min max)**
  - Shows "List schedules" via voice query
  - Shows "Book appointment" via voice command
  - Shows confirmation/response
  - Audio is clear
  - File format: MP4 or WebM
  - File size: < 100 MB

- [ ] **Documentation**
  - README.md updated with GitHub link
  - Demo usage examples documented
  - API endpoints documented

---

## Troubleshooting

### Recording Audio Issues
- Check system volume is at 100%
- Test microphone in Windows Settings → Sound
- Use Chrome DevTools (F12) to verify audio is being captured

### App Not Responding to Voice
- Ensure you're using Chrome/Chromium
- Check microphone permissions in browser
- Test by saying commands clearly and slowly
- Check Flask console for error messages

### GitHub Push Fails
```
# If "fatal: remote origin already exists":
git remote rm origin
git remote add origin https://github.com/YOUR_USERNAME/voice-automation-agent.git
git push -u origin main
```

---

## Sample Demo Script (to memorize)

```
INTRO:
"This is a voice-powered clinic appointment system. I can list available appointments 
and book new ones entirely through voice commands."

LIST COMMAND:
"Let me ask the system for tomorrow's available appointments."
[Click Start Listening]
[Say: "What appointments are available tomorrow?"]
[Wait for response, show results]

BOOKING COMMAND:
"Now let me book a new appointment for tomorrow at 2 PM."
[Click Start Listening]
[Say: "Book an appointment for tomorrow at 2 PM"]
[Wait for confirmation]

VERIFICATION:
"The appointment has been successfully added to the system. 
This demonstrates the voice-powered scheduling capability."
```

---

## Next Steps

1. **Create GitHub repo** (using "Step-by-Step" above)
2. **Record demo** (using "Recording Instructions")
3. **Get GitHub link** and **get recording link**
4. **Submit both** for assessment

Good luck! 🎉
