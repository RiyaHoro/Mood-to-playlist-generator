from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from emotion_classifier import get_mood
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV
df = pd.read_csv("emotions.csv")

class MoodText(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Mood-to-Playlist API is running!"}


@app.post("/predict")
def predict_mood(data: MoodText):
    mood = get_mood(data.text)

    # Filter matching songs
    songs = df[df["mood"] == mood].sample(min(5, len(df[df["mood"] == mood]))).to_dict("records")

    return {
        "input": data.text,
        "mood": mood,
        "playlist": songs
    }
