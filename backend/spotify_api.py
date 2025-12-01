import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_client():
    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not CLIENT_ID or not CLIENT_SECRET:
        raise Exception("Spotify API credentials not found")

    auth_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)
