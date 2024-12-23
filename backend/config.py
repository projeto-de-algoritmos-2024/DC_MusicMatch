# backend/config.py
import os

class SpotifyConfig:
    CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID', "fc4ebaa07ae441d1aeefe351977b893b")
    CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET', "b183110d72ae4ee880da7fb76234488e")
    REDIRECT_URI = "http://localhost:5000/callback"
