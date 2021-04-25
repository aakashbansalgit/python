import speech_recognition as sr
import os
import pydub

mp3file = "assignment.mp3"
wavfile = "assignment.wav"

sound = pydub.AudioSegment.from_mp3(mp3file)
sound.export(wavfile, format="wav")                                                     

AUDIO_FILE = "assignment.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))
