#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import base64

def busca_online(query):
    """
    Realiza uma busca online usando uma API de busca
    
    Args:
        query (str): A pergunta a ser pesquisada
        
    Returns:
        str: O resultado da busca ou "No Result!" se não encontrar nada
    """
    try:
        search_url = f"https://ddg-api.herokuapp.com/search?query={query}&limit=1"
        response = requests.get(search_url)
        
        if response.status_code != 200:
            return "No Result!"
        
        data = response.json()
        if not data or 'body' not in data[0]:
            return "No Result!"
        
        return data[0]['body']
    except Exception as e:
        print(f"Erro na busca: {e}")
        return "No Result!"

if __name__ == "__main__":
    # Teste da função
    resultado = busca_online("Quem é o presidente do Brasil")
    print(resultado)
