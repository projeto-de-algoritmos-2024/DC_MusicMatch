from flask import Flask, render_template, request, jsonify
from backend.match_manager import MatchManager
from backend.user_manager import UserManager

app = Flask(__name__)
match_manager = MatchManager()
user_manager = UserManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_match')
def create_match():
    return render_template('match.html')

@app.route('/view_matches')
def view_matches():
    matches = []
    return render_template('match.html', matches=matches)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/process_match', methods=['POST'])
def process_match():
    data = request.json
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
