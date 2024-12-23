from .models.match import Match
import uuid
from datetime import datetime

class MatchManager:
    def __init__(self):
        self.matches = {}
        
    def get_all_matches(self):
        """
        Retorna todos os matches ordenados por data de criação
        """
        matches_list = []
        for match_id, match_data in self.matches.items():
            if match_data.get('playlist1') and match_data.get('playlist2'):
                matches_list.append({
                    'id': match_id,
                    'name': f"Match #{match_id[:8]}",
                    'similarity': match_data.get('similarity', 0),
                    'created_at': match_data.get('created_at', datetime.now())
                })
        return sorted(matches_list, key=lambda x: x['created_at'], reverse=True)

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

class MatchAnalyzer:
    def __init__(self, playlist1, playlist2):
        self.playlist1 = playlist1
        self.playlist2 = playlist2

    def calculate_similarity(self):
        # Implementação usando Divisão e Conquista
        return self._similarity_dc(self.playlist1, self.playlist2, 0, len(self.playlist1))

    def _similarity_dc(self, list1, list2, start, end):
        # Caso base
        if end - start <= 3:
            return self._direct_similarity(list1[start:end], list2[start:end])

        # Divisão
        mid = (start + end) // 2
        
        # Conquista
        left_sim = self._similarity_dc(list1, list2, start, mid)
        right_sim = self._similarity_dc(list1, list2, mid, end)
        
        # Combinação usando mediana das medianas
        return self._combine_similarities(left_sim, right_sim)

    def _combine_similarities(self, sim1, sim2):
        # Usando Karatsuba para multiplicação de similaridades
        return (sim1 + sim2) / 2

    def get_common_tracks(self):
        return list(set(self.playlist1) & set(self.playlist2))
