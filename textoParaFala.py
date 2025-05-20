# -*- coding: utf-8 -*-

import os
from gtts import gTTS
from playsound import playsound

def textoParaFala(texto, tocar = True, excluir = True, caminho = "./audio.mp3"):
    try:
        tts = gTTS(texto, lang = "pt-br")
        tts.save(caminho)
        if os.path.exists(caminho) and tocar:
            playsound(caminho)
    except Exception as e:
        print("error:", e)
    finally:        
        if os.path.exists(caminho) and excluir:
            os.remove(caminho)
        if not os.path.exists(caminho):
            caminho = None
    return caminho

# print(textoParaFala("Meu nome é Matheus"))
