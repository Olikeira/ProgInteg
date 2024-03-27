from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)


def conectar_bd():
    """Estabelece uma conexão com o banco de dados SQLite."""
    return sqlite3.connect('bauru_participa.db')


def inicializar_bd():
    """Inicializa o banco de dados SQLite com as tabelas necessárias."""
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enquetes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS opcoes_enquete (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                enquete_id INTEGER,
                opcao TEXT NOT NULL,
                votos INTEGER DEFAULT 0,
                FOREIGN KEY (enquete_id) REFERENCES enquetes(id)
            )
        ''')
        conexao.commit()


@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    """Endpoint para criar uma nova enquete."""
    dados = request.get_json()
    titulo = dados.get('titulo')
    descricao = dados.get('descricao')
    if not titulo or not descricao:
        abort(400, 'Título e descrição são obrigatórios')
    
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO enquetes (titulo, descricao) VALUES (?, ?)', (titulo, descricao))
        id_enquete = cursor.lastrowid
        conexao.commit()
    
    return jsonify({'mensagem': 'Enquete criada com sucesso', 'id_enquete': id_enquete}), 201


@app.route('/api/enquetes', methods=['GET'])
def listar_enquetes():
    """Endpoint para listar todas as enquetes."""
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT id, titulo, descricao FROM enquetes')
        enquetes = cursor.fetchall()
    
    return jsonify({'enquetes': enquetes})


@app.route('/api/enquetes/<int:id>', methods=['GET'])
def detalhes_enquete(id):
    """Endpoint para recuperar detalhes de uma enquete específica identificada pelo seu ID."""
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT id, titulo, descricao FROM enquetes WHERE id=?', (id,))
        enquete = cursor.fetchone()
        if not enquete:
            abort(404, 'Enquete não encontrada')
        
        cursor.execute('SELECT id, opcao, votos FROM opcoes_enquete WHERE enquete_id=?', (id,))
        opcoes = cursor.fetchall()
    
    return jsonify({'enquete': enquete, 'opcoes': opcoes})
