def test_audio():
    # initialize Text-to-speech engine
    #engine = pyttsx3.init()
    # convert this text to speech
    text = "Python is a great programming language"

    # setting new voice rate (faster)
    engine.setProperty("rate", 300)
    engine.say(text)
    # play the speech
    engine.runAndWait()

def test_audio2():
    # make request to google to get synthesis
    tts = gtts.gTTS("Hello world", lang="fr")
    # save the audio file
    tts.save("hello.mp3")
    # play the audio file
    playsound("hello.mp3")


import pyttsx3
# initialize Text-to-speech engine test_audio
engine = pyttsx3.init()

#test_audio 2
import gtts
from playsound import playsound

def test_audio():
    # initialize Text-to-speech engine
    #engine = pyttsx3.init()
    # convert this text to speech
    text = "Python is a great programming language"

    # setting new voice rate (faster)
    engine.setProperty("rate", 300)
    engine.say(text)
    # play the speech
    engine.runAndWait()

def test_audio2():
    # make request to google to get synthesis
    tts = gtts.gTTS("Bonjour, comment allez vous", lang="fr")
    # save the audio file
    tts.save("hello.mp3")
    # play the audio file
    playsound("hello.mp3")
