import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id="55335836649141f5bd8353b0c3183d8a",
        client_secret="3f3e08de9be34dc6922d6afc232bfc3f"
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp
