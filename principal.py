# -*- coding: utf-8 -*-

import os
from falaParaTexto import falaParaTexto
from textoParaFala import textoParaFala
from busca_online import busca_online

def main():
    print("Assistente Virtual - Versão macOS")
    print("Digite 'sair' para encerrar o programa")
    
    while True:
        print("\nFaça uma pergunta...")
        pergunta = falaParaTexto()
        
        # Opção para sair do programa
        if pergunta.lower() == "sair":
            print("Encerrando o assistente virtual...")
            break
            
        print(f"Buscando resposta para: {pergunta}")
        resultado = busca_online(pergunta)
        
        if resultado == "No Result!":
            resultado = "Não encontrei nada, tente novamente"
            
        print(f"Resultado: {resultado}")
        textoParaFala(resultado)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print(f"\nErro: {e}")

