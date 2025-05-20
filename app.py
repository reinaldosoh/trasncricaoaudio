#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Garantir que o diretório de transcrições existe
os.makedirs('transcricoes', exist_ok=True)

# Rota principal que serve a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para verificar se a API está funcionando
@app.route('/api/status')
def status():
    return jsonify({
        'status': 'online',
        'message': 'API de transcrição de áudio está funcionando!'
    })

# Rota para salvar transcrição (opcional)
@app.route('/api/save-transcript', methods=['POST'])
def save_transcript():
    data = request.json
    if not data or 'transcript' not in data:
        return jsonify({'success': False, 'error': 'Dados inválidos'}), 400
    
    transcript = data['transcript']
    filename = data.get('filename', 'transcript.txt')
    
    try:
        with open(os.path.join('transcricoes', filename), 'w', encoding='utf-8') as f:
            f.write(transcript)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Necessário para Vercel
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Para desenvolvimento local
if __name__ == '__main__':
    app.run(debug=True, port=5000)
