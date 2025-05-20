#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

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

# Necessário para Vercel
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Para desenvolvimento local
if __name__ == '__main__':
    app.run(debug=True, port=5000)
