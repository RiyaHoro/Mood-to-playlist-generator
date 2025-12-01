# 🎧 Mood-to-Playlist Generator

An AI-powered web application that detects your **mood** from text + emojis and recommends a **personalized music playlist**.  
It uses **FastAPI (Python)** for the backend mood detection and **React** for the frontend UI.

---

## 🌟 Demo
Coming soon…

---

## 🚀 Features

- 🎭 **Emotion Detection**
  - Detects emotions using text analysis
  - Emoji-based mood detection (😔😊😍😴🤬 etc.)

- 🎵 **AI Playlist Recommendation**
  - Maps mood → curated list of songs
  - Spotify/Youtube links

- ⚡ **FastAPI Backend**
  - Clean `/predict` endpoint
  - CSV-based music data

- 💜 **React Frontend**
  - Aesthetic UI
  - Responsive layout

- 🌍 **Cross-Origin Support**
  - Fully enabled CORS for frontend-backend communication

---

## 🧠 How It Works

1. User enters → *mood text* or *emojis*  
   Example: `"Feeling low 😔"`

2. FastAPI backend:
   - Detects mood using emoji/keyword rules  
   - Fetches matching playlist from CSV

3. Frontend:
   - Displays mood + recommended songs
   - Buttons to open Spotify/Youtube

---

## 🛠️ Tech Stack

### **Frontend**
- React (JavaScript)
- Axios API calls
- Custom CSS

### **Backend**
- Python 3
- FastAPI
- Uvicorn
- Pandas
- Emoji library

### **Deployment**
- Backend → Render  
- Frontend →  Vercel

---

## 📁 Folder Structure
```
Mood-to-Playlist-Generator/
│
├── backend/
│ ├── main.py
│ ├── emotion_classifier.py
│ ├── emotions.csv
│ ├── requirements.txt
│
└── frontend/
├── src/
│ ├── App.jsx
│ ├── MoodInput.jsx
│ ├── Playlist.jsx
│ ├── api.js
│ └── index.css
```

---

## ▶️ Running the Project Locally

### **1. Clone Repo**
git clone https://github.com/
<your-username>/Mood-to-playlist-generator.git
cd Mood-to-playlist-generator


---

## 🔹 Backend Setup (FastAPI)

### **2. Create Virtual Environment**


cd backend
python -m venv venv
venv/Scripts/activate # Windows
source venv/bin/activate # Mac/Linux


### **3. Install Requirements**


pip install -r requirements.txt


### **4. Run FastAPI**


uvicorn main:app --reload


Backend runs at:


http://127.0.0.1:8000


Docs:


http://127.0.0.1:8000/docs


---

## 🔹 Frontend Setup (React)



cd frontend
npm install
npm start


Frontend runs at:


http://localhost:3000


---

## 📡 API Reference

### **POST /predict**
Predict mood from text.

#### **Request Body**
```json
{
  "text": "I feel happy today 😊"
}

Response
{
  "mood": "happy",
  "playlist": [
    {
      "song": "Happy",
      "artist": "Pharrell Williams",
      "link": "https://..."
    }
  ]
}
```

### 🎨 Screenshots
Render deployment screenshot
![image](/frontend/src/assets/img.png)

![Alt text](/frontend/src/assets/image1.png)
📌 App Screenshot
![img](/frontend/src/assets/im.png)

## 💡 Future Enhancements
```
Spotify API integration

User mood history

Weekly mood dashboard

Advanced ML model (SVM/LogReg)

Animated UI
```

## ❤️ Contributing

Pull requests are welcome.

## 📄 License

This project is open-source and free to use.
