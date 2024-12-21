from datetime import datetime

class Match:
    def __init__(self, match_id, playlist1, playlist2):
        self.id = match_id
        self.playlist1 = playlist1
        self.playlist2 = playlist2
        self.similarity = self._calculate_similarity()
        self.created_at = datetime.now()
        self.name = f"Match {self.created_at.strftime('%Y%m%d')}"
    
    def _calculate_similarity(self):
        common = set(self.playlist1) & set(self.playlist2)
        total = set(self.playlist1) | set(self.playlist2)
        return len(common) / len(total) if total else 0
    
    def rename(self, new_name):
        self.name = new_name
