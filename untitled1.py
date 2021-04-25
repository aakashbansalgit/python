import speech_recognition as sr
from pydub import AudioSegment

#first we convert audio file format from mp3 to wav                                                        
sound = AudioSegment.from_mp3("assignment.mp3")
sound.export("assignment.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "assignment.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))
