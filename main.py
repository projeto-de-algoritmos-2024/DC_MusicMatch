from flask import Flask, render_template, request, jsonify
from backend.match_manager import MatchManager
from backend.user_manager import UserManager
import uuid
from backend.spotify_manager import SpotifyManager
from backend.match_manager import MatchManager, MatchAnalyzer


app = Flask(__name__)
match_manager = MatchManager()
user_manager = UserManager()
spotify_manager = SpotifyManager()  # Nova instância

@app.route('/')
def home():
    return render_template('index.html')

# main.py
@app.route('/create_match')
def create_match():
    return render_template('create_match.html')  # Novo template

@app.route('/view_matches')
def view_matches():
    matches = match_manager.get_all_matches()  # Obter todos os matches
    return render_template('view_matches.html', matches=matches)  # Usar template correto



@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/process_match', methods=['POST'])
def process_match():
    data = request.json
    playlist1 = data.get('playlist1', [])
    playlist2 = data.get('playlist2', [])
    
    try:
        match = match_manager.create_match(playlist1, playlist2)
        return jsonify({
            'status': 'success',
            'match_id': match.id,
            'similarity_score': match.similarity_score,
            'match_name': match.name
        })
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500
    
# main.py (adicionar nova rota)
@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'POST':
        playlist_data = request.json
        match_id = str(uuid.uuid4())
        share_link = f"{request.host_url}join/{match_id}"
        
        match_manager.save_playlist(match_id, playlist_data)
        return jsonify({
            'status': 'success',
            'share_link': share_link
        })
    
    return render_template('create_playlist.html')

@app.route('/search_tracks', methods=['POST'])
def search_tracks():
    data = request.json
    query = data.get('query', '')
    tracks = spotify_manager.search_tracks(query)
    return jsonify({'tracks': tracks})

@app.route('/join/<match_id>')
def join_match(match_id):
    match = match_manager.get_match(match_id)
    if not match:
        # Se não encontrar o match, criar um novo
        match = {
            'id': match_id,
            'playlist1': None,
            'playlist2': None,
            'status': 'pending'
        }
        match_manager.matches[match_id] = match
    
    # Verifica se já tem duas playlists
    if match.get('playlist2'):
        return "Este match já está completo", 400
        
    return render_template('create_playlist.html', 
                         match_id=match_id, 
                         is_second_user=bool(match.get('playlist1')))


@app.route('/finalize_playlist', methods=['POST'])
def finalize_playlist():
    data = request.json
    match_id = str(uuid.uuid4())
    playlist = data.get('songs', [])
    
    try:
        match_manager.save_playlist(match_id, playlist)
        share_link = request.host_url + 'join/' + match_id
        return jsonify({
            'status': 'success',
            'share_link': share_link
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/match_result/<match_id>')
def match_result(match_id):
    match = match_manager.get_match(match_id)
    if not match:
        return "Match não encontrado", 404

    analyzer = MatchAnalyzer(match['playlist1'], match['playlist2'])
    similarity = analyzer.calculate_similarity()
    common_tracks = analyzer.get_common_tracks()

    return render_template('match_result.html',
                         similarity_percentage=int(similarity * 100),
                         common_tracks=common_tracks)


if __name__ == '__main__':
    app.run(debug=True)
