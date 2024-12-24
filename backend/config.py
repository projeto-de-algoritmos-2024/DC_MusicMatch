# backend/config.py
import os

class SpotifyConfig:
    CLIENT_ID = os.getenv('Seu Client', "fc4ebaa07ae441d1aeefe351977b893b")
    CLIENT_SECRET = "Seu Client")
    REDIRECT_URI = "http://localhost:5000/callback"
