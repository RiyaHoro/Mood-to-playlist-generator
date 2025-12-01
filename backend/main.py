from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from emotion_classifier import get_mood
from spotify_api import get_spotify_client
from mood_to_genre import MOOD_GENRE_MAP

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # IMPORTANT
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MoodText(BaseModel):
    text: str
import os

@app.get("/check-env")
def check_env():
    return {
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET")
    }

@app.post("/predict")
def predict_mood(data: MoodText):
    try:
        mood = get_mood(data.text)

        from spotify_api import get_spotify_client
        from mood_to_genre import MOOD_GENRE_MAP

        sp = get_spotify_client()
        genres = MOOD_GENRE_MAP.get(mood, ["pop"])

        results = sp.recommendations(seed_genres=genres, limit=10)

        # If Spotify returns no tracks
        if not results or "tracks" not in results:
            return {"error": "Spotify returned no tracks", "raw": results}

        playlist = []
        for track in results["tracks"]:
            playlist.append({
                "song": track["name"],
                "artist": track["artists"][0]["name"],
                "link": track["external_urls"]["spotify"],
                "preview": track["preview_url"],
                "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None
            })

        return {"mood": mood, "playlist": playlist}

    except Exception as e:
        return {"error": str(e)}

    