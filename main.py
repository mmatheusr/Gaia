# our main py

import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

#Abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #define microfone como fonte de Áudio
   
        print(r.recognize_google(audio, language='pt'))
    