# our main py

from vosk import Model, KaldiRecognizer
import os
import json
import pyaudio
import pyttsx3

# Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(texto):
    engine.say("eu falo esse texto")
    engine.runAndWait()
# end def

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
        result = json.loads(result)

        if result is not None:
            text = result['text']

        print(texto)
        speak(texto)