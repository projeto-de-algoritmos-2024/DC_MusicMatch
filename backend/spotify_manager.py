
# backend/spotify_manager.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .config import SpotifyConfig
import json
from typing import List, Dict

class SpotifyManager:
    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=SpotifyConfig.CLIENT_ID,
            client_secret=SpotifyConfig.CLIENT_SECRET
        )
        self.spotify = spotipy.Spotify(
            client_credentials_manager=self.client_credentials_manager
        )

    def search_tracks(self, query: str) -> List[Dict]:
        try:
            results = self.spotify.search(q=query, type='track', limit=10)
            return self._format_tracks(results['tracks']['items'])
        except Exception as e:
            print(f"Erro na busca: {str(e)}")
            return []

    def _format_tracks(self, tracks: List[Dict]) -> List[Dict]:
        return [{
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'preview_url': track['preview_url']
        } for track in tracks]
