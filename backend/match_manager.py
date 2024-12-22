from .models.match import Match
import uuid

class MatchManager:
    def __init__(self):
        self.matches = {}
    
    def create_match(self, playlist1, playlist2):
        match_id = str(uuid.uuid4())
        match = Match(match_id, playlist1, playlist2)
        self.matches[match_id] = match
        return match
    
    def get_match(self, match_id):
        return self.matches.get(match_id)
