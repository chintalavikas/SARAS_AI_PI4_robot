from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

model = Model("models/vosk-model-small-en-us")
rec = KaldiRecognizer(model, 16000)

with sd.RawInputStream(samplerate=16000, blocksize=8000,
                       dtype='int16', channels=1, callback=callback):

    print("Listening...")

    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            print("You said:", result["text"])