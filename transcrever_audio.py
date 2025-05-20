#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

def transcrever_audio(max_tentativas=5):
    """
    Captura áudio do microfone e transcreve para texto.
    
    Args:
        max_tentativas (int): Número máximo de tentativas de reconhecimento
        
    Returns:
        str: O texto transcrito ou string vazia se falhar
    """
    # Inicializa o reconhecedor
    reconhecedor = sr.Recognizer()
    
    # Lista os microfones disponíveis
    print("\nMicrofones disponíveis:")
    for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {mic_name}")
    
    # Captura áudio do microfone
    with sr.Microphone() as fonte_audio:
        print("\nAjustando para ruído ambiente...")
        reconhecedor.adjust_for_ambient_noise(fonte_audio)
        
        for tentativa in range(max_tentativas):
            try:
                print(f"\nTentativa {tentativa+1}/{max_tentativas}. Fale agora...")
                audio = reconhecedor.listen(fonte_audio)
                
                print("Processando o áudio...")
                texto = reconhecedor.recognize_google(audio, language="pt-BR")
                
                print(f"Texto transcrito: {texto}")
                return texto
                
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio")
            except sr.RequestError as e:
                print(f"Erro na requisição ao serviço de reconhecimento: {e}")
            except Exception as e:
                print(f"Erro: {e}")
        
        print("Número máximo de tentativas alcançado.")
        return ""

# Executar diretamente
print("=== Transcrição de Áudio para Texto ===")
print("Fale após o aviso. Pressione Ctrl+C para sair.")

try:
    while True:
        print("\nIniciando nova transcrição...")
        texto = transcrever_audio()
        if texto:
            print(f"\nResultado final: {texto}")
        print("-----------------------------------")
        
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
