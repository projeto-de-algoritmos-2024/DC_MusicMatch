class InfoManager:
    def __init__(self):
        self.app_info = {
            "name": "Music Match",
            "version": "1.0.0",
            "description": "Aplicação para encontrar similaridades musicais",
            "features": [
                "Criação de matches musicais",
                "Análise de similaridade",
                "Compartilhamento de playlists"
            ]
        }
    
    def get_info(self):
        return self.app_info
