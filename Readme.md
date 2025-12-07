# 🎧 Mood-to-Playlist Generator

An AI-powered web application that detects your **mood** from text + emojis and recommends a **personalized music playlist**.  
It uses **FastAPI (Python)** for the backend mood detection and **React** for the frontend UI.

---

## 🌟 Demo
Live Demo:
🔗 Frontend: https://mood-to-playlist-generator.vercel.app

🔗 Backend: https://mood-to-playlist-generator.onrender.com
---

## 🚀 Features

- 🎭 Emotion Detection

  Detects mood using text-based keyword matching

  Emoji-based mood detection (😔 😊 😍 😴 🤬 etc.)

- 🎵 Playlist Recommendation

  Maps mood → genre (happy → pop, sad → soft, angry → rock, etc.)

  Fetches real music tracks using the Spotify Search API

  Includes song name, artist, album image, preview URL

- ⚡ FastAPI Backend

  Clean /predict endpoint

  Emoji + keyword mood recognition

  Spotify Search API integration

  CORS enabled for frontend communication

- 💜 React Frontend

  Modern, clean UI

  Mood input box

  Playlist display with clickable Spotify links

- 🌍 Cross-Origin Support

    Fully enabled CORS for frontend → backend requests

---

## 🧠 How It Works
1. User Input

The user enters text or emojis:

  “I feel low 😔”
  “So happy today! 😊”

2. FastAPI Backend

  Reads emojis → maps to mood

  Reads keywords → maps to mood

  Mood → mapped to genre using MOOD_GENRE_MAP

Spotify API is used: sp.search(q="genre:pop", type="track", limit=10)

3. React Frontend

Displays the detected mood

Shows recommended playlist from Spotify

Each song includes:
-
Title

Artist

Spotify link

Preview URL

Album cover

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
│   ├── main.py
│   ├── emotion_classifier.py
│   ├── spotify_api.py
│   ├── mood_to_genre.py
│   ├── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── MoodInput.jsx
    │   ├── Playlist.jsx
    │   ├── api.js
    │   └── index.css

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
Full Spotify OAuth integration

Save mood history

Weekly mood dashboard

Machine learning–based emotion detection

Animated UI improvements
```

## ❤️ Contributing

Pull requests are welcome.

## 📄 License

This project is open-source and free to use.
