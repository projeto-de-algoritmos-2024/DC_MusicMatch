class UserManager:
    def __init__(self):
        self.users = {}
        
    def create_user(self, user_id, name):
        self.users[user_id] = {
            'name': name,
            'matches': [],
            'playlists': []
        }
        return self.users[user_id]
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def add_match(self, user_id, match_id):
        if user_id in self.users:
            self.users[user_id]['matches'].append(match_id)
            
    def get_user_matches(self, user_id):
        if user_id in self.users:
            return self.users[user_id]['matches']
        return []
