from .models.match import Match
import uuid
import datetime

class MatchManager:
    def __init__(self):
        self.matches = {}

    def create_match(self, playlist1, playlist2):
        if not playlist1 or not playlist2:
            raise ValueError("Ambas as playlists devem conter músicas")

        try:
            match_id = str(uuid.uuid4())
            match = Match(match_id, playlist1, playlist2)
            self.matches[match_id] = match
            
            # A similaridade já é calculada no construtor de Match
            similarity_score = match.similarity
            
            # Converter a similaridade para porcentagem
            match.similarity_score = round(similarity_score * 100, 2)
            
            return match
        except Exception as e:
            # Log do erro e re-lançamento da exceção
            print(f"Erro ao criar match: {str(e)}")
            raise
    
    def save_playlist(self, match_id, playlist_data):
        """
        Salva uma playlist para um match específico
        """
        if not match_id or not playlist_data:
            raise ValueError("Match ID e dados da playlist são obrigatórios")
            
        try:
            playlist = {
                'id': match_id,
                'tracks': playlist_data.get('songs', []),
                'created_at': datetime.now(),
                'status': 'pending'  # pending até que a segunda pessoa crie sua playlist
            }
            
            # Armazena a playlist no dicionário de matches
            if match_id not in self.matches:
                self.matches[match_id] = {
                    'playlist1': playlist,
                    'playlist2': None,
                    'similarity': None
                }
            else:
                # Se já existe playlist1, salva como playlist2 e calcula similaridade
                self.matches[match_id]['playlist2'] = playlist
                self._calculate_match_similarity(match_id)
                
            return True
            
        except Exception as e:
            print(f"Erro ao salvar playlist: {str(e)}")
            return False

    def _calculate_match_similarity(self, match_id):
        """
        Calcula a similaridade entre as playlists de um match
        """
        match = self.matches.get(match_id)
        if match and match['playlist1'] and match['playlist2']:
            tracks1 = set(track['id'] for track in match['playlist1']['tracks'])
            tracks2 = set(track['id'] for track in match['playlist2']['tracks'])
            
            # Usando divisão e conquista para calcular similaridade
            similarity = self._calculate_similarity_dc(list(tracks1), list(tracks2))
            match['similarity'] = similarity
            match['status'] = 'completed'




    def get_match(self, match_id):
        return self.matches.get(match_id)

    def calculate_similarity(self, playlist1, playlist2):
        # Implementação do cálculo de similaridade
        common_tracks = set(playlist1) & set(playlist2)
        total_tracks = set(playlist1) | set(playlist2)
        
        if not total_tracks:
            return 0
        
        similarity = len(common_tracks) / len(total_tracks)
        return round(similarity * 100, 2)  # Retorna a porcentagem de similaridade
