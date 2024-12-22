class MatchUI {
    constructor() {
        this.matchContainer = document.getElementById('match-container');
    }

    createMatchCard(match) {
        return `
            <div class="match-card">
                <h3>${match.name}</h3>
                <p>Similaridade: ${(match.similarity * 100).toFixed(2)}%</p>
                <button onclick="editMatch('${match.id}')">Editar</button>
            </div>
        `;
    }
}
