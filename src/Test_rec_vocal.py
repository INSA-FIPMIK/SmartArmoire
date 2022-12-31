#text = r.recognize_google(audio, language="fr-FR")

#import library
#import simpleaudio as sa
#import simpleaudio.functionchecks as fc

import speech_recognition as sr
#import sounddevice as sd
#from scipy.io.wavfile import write

import pyttsx3

# initialize Text-to-speech engine test_audio
engine = pyttsx3.init()


#test_audio 2
import gtts
from playsound import playsound

##Debut_enregistrement = 'Debut_Enregistrement.wav'
##Bienvenu = 'Bienvenu.wav'
##Question1 = 'Question_1.wav'
##Question2 = 'Question_2.wav'
##Question3 = 'Question_3.wav'
##Question4 = 'Question_4.wav'
##Final = 'Final.wav'

Debut_enregistrement = "C'est a vous, parler"
Bienvenu = "Bonjour, quelle porte voulez-vous ouvrir"
Question1 = "Quelle est la réponse ?"
Question2 = "Quelle est la réponse 2?"
Question3 = "Quelle est la réponse 3?"
Question4 = "Quelle est la réponse 4?"
Final = 'Vous avez répondu correctement, merci'

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

def comprehension_audio(wave):
    r = sr.Recognizer()
    with sr.WavFile(wave) as source:
        audio = r.record(source)
        
##    with sr.Microphone() as source:
##        faire_audio(Debut_enregistrement)
##        print("Dites quelque chose")
##        audio = r.listen(source)
        
        texte = r.recognize_google(audio, language='fr-FR')
        print("Retranscription: " + texte)
        
        """try:
            texte = r.recognize_google(audio, language='fr-FR', show_all=False)
            print('Transcription GOOGLE: ' + texte )
        except LookupError:
                print("L'audio n'as pas été compris")
        except sr.UnknownValueError:
            print("L'audio n'as pas été compris")
        except sr.RequestError as e:
            print("Le service Google Speech API ne fonctionne plus" + format(e))
            """
    return texte


def faire_audio(nbr):
    Audio_file = question(nbr)
    
    # utilisation Audio_file deja enregistré
    # directly from WAV files on disk
    wave_obj = sa.WaveObject.from_wave_file(Audio_file)   
     
    # Audio playback
    play = wave_obj.play()
               
    # To stop after playing the whole audio
    play.wait_done() 
    play.stop()
    
def question(num_question):
    switch={
       0: Bienvenu,
       1: Question1,
       2: Question2,
       3: Question3,
       4: Question4,
       5: Final,
       }
    return switch.get(num_question)

def rep(num_question):
    switch={
       0: 'Bonjour',
       1: 'truc',
       2: 'singe',
       3: 'rep3',
       4: 'rep1',
       5: 'merci',
       }
    return switch.get(num_question)

def verif(texte,nbr):
    ok = 0
    reponse = rep(nbr)
    if reponse in texte:
        print("Correct")
        ok = 1
    elif 'repeter' in texte:
        print("repeter")
        ok = 2
    elif 'quitter' in texte:
        print("repeter")
        ok = 3
    else:
        print("Faux")
        ok = 0
    return ok

def debut():
    num_question = 0
    #Emission audio
    #faire_audio(num_question)
    test_audio()
    #Enregistrement
    WAVFILE = 'test3.wav'
    # Test de comprehension fichier audio
    texte = comprehension_audio(WAVFILE)
    print("fin debut")

def QandR():
    #Debut
    num_question = 1
    while num_question < 5:
        #Emission audio
        #faire_audio(num_question)
        test_audio()
        print("audio")
        #Enregistrement
        WAVFILE = 'racailles.wav'
        # Test de comprehension fichier audio
        texte = comprehension_audio(WAVFILE)
        #Detection avec phrase contient
        OK = verif(texte, num_question)
        if OK == 1:
            num_question = num_question + 1
        elif OK == 3:
            num_question = 5
        elif OK == 2:
            num_question = num_question
            #Repasse la meme question
        elif OK== 0:
            num_question = num_question + 1
            #A changer, possibilité de refaire la meme ou quitter
    return OK

debut()
#ok = QandR()


##myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
##sd.wait()  # Wait until recording is finished
##write('output.wav', fs, myrecording)  # Save as WAV file
##
