# -*- coding: utf-8 -*-

import speech_recognition as sr

print("\r\nMicrofones: " + str(sr.Microphone.list_microphone_names()) + "\r\n")

def falaParaTexto(texto = "", max_contador = 5):    
    contador = 0
    microfone = sr.Recognizer()
    with sr.Microphone() as canal:
        microfone.adjust_for_ambient_noise(canal)
        while contador < max_contador:
            try:
                contador += 1
                print("Ouvindo...")
                audio = microfone.listen(canal)
                texto = microfone.recognize_google(audio, language = "pt-BR")                
                break
            except Exception as e:
                print("error:", e)
    print("Entendi: " + texto)
    return texto

# print(falaParaTexto())
