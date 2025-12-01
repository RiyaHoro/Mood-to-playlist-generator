from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from emotion_classifier import get_mood
from spotify_api import get_spotify_client
from mood_to_genre import MOOD_GENRE_MAP

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoodText(BaseModel):
    text: str

@app.post("/predict")
def predict_mood(data: MoodText):
    mood = get_mood(data.text)

    sp = get_spotify_client()
    genres = MOOD_GENRE_MAP.get(mood, ["pop"])

    # Get 10 recommended tracks
    results = sp.recommendations(seed_genres=genres, limit=10)

    playlist = []
    for track in results["tracks"]:
      playlist.append({
        "song": track["name"],
        "artist": track["artists"][0]["name"],
        "link": track["external_urls"]["spotify"],
        "preview": track["preview_url"],
        "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None
    })

    return {
        "mood": mood,
        "playlist": playlist
    }
