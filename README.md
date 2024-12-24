# MatchMusic

**Número da Lista**: 38<br>
**Conteúdo da Disciplina**: Dividir e Conquistar<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/1021975  |  Gabriel Santos Monteiro |

## Sobre 
Este projeto visa criar uma aplicação web que permite fazer match de gostos musicais entre duas pessoas, utilizando o algoritmo de Divisão e Conquista para analisar e comparar as preferências musicais. A aplicação integra com a API do Spotify para buscar músicas e criar playlists personalizadas baseadas na similaridade dos gostos musicais dos usuários.

## Screenshots

| Tela de Introdução                         | Tela de Procurar Música                           |
| ------------------------------------------ | ------------------------------------------ |
| ![Intro](./static/img/inicio.png)                    | ![Search](./static/img/procurar.png)                      |

| Tela de Informações                     | Tela de Fim de Jogo                        |
| ------------------------------------------ | ------------------------------------------ |
| ![Infos](/./static/img/infos.png)                    | ![Select](./static/img/selecionar.png)                        |

| Tela de Matches                     |
| ------------------------------------------ |
| ![Infos](./static/img/matches.png)                    |


## Instalação 
**Linguagem**: Python<br>
**Framework**: Flask<br>

### Dependências
```bash
pip install flask
pip install spotipy
pip install sqlite3
```

### Configuração
1. Crie uma conta no Spotify Developers
2. Configure as credenciais do aplicativo
3. Adicione CLIENT_ID e CLIENT_SECRET no arquivo config.py

## Uso 
1. Execute o servidor Flask:
```bash
python main.py
```
2. Acesse http://localhost:5000
3. Crie sua playlist selecionando músicas
4. Compartilhe o link gerado com um amigo
5. Após o amigo criar sua playlist, o algoritmo calculará a similaridade

## Outros 
O projeto utiliza:
- Algoritmo de Divisão e Conquista para análise de similaridade
- API do Spotify para busca de músicas
- Interface interativa com tema espacial
- Sistema de compartilhamento via links
- Banco de dados SQLite para persistência

## Apresentação Vídeo

<a href="https://youtu.be/xn90uF7eCIk?si=v-bqYmDnZ8ZBYxH_">
 <img src="https://img.youtube.com/vi/xn90uF7eCIk?si=v-bqYmDnZ8ZBYxH_/0.jpg" alt="Título do Vídeo" width="240" height="180" border="10" />
</a>

