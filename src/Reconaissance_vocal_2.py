#text = r.recognize_google(audio, language="fr-FR")

# import library
import simpleaudio as sa
import simpleaudio.functionchecks as fc

import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

Debut_enregistrement = 'Debut_Enregistrement.wav'
Bienvenu = 'Bienvenu.wav'
Question1 = 'Question_1.wav'
Question2 = 'Question_2.wav'
Question3 = 'Question_3.wav'
Question4 = 'Question_4.wav'
Final = 'Final.wav'


def comprehension_audio(): 
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        faire_audio(Debut_enregistrement)
        print("Dites quelque chose")
        audio = r.listen(source)
    try:
        texte = r.recognize_google(audio, language='fr-FR', show_all=False)
        print('Transcription GOOGLE: ' + texte )
    except LookupError:
            print("L'audio n'as pas été compris")
    except sr.UnknownValueError:
        print("L'audio n'as pas été compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))
    return texte


def faire_audio(Audio_file): 
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
       '0': Bienvenu,
       '1': Question1,
       '2': Question2,
       '3': Question3,
       '4': Question4,
       '5': Final,
       }
    return switch.get(num_question,'Question en cours: ')

def reponse_question(reponse):
    switch={
       '0': 'Bonjour',
       '1': 'Question 1',
       '2': 'Question 1',
       '3': 'Question 1',
       '4': 'Question 1',
       }
    return switch.get(num_question,'Question en cours: ')

def commande(texte):
    switch={
       'Ouvrir porte 1': 11,
       'Ouvrir porte 2': 12,
       'Ouvrir porte 3': 13,
       'Ouvrir porte 4': 14,
       'Fermer porte 1': 21,
       'Fermer porte 2': 22,
       'Fermer porte 3': 23,
       'Fermer porte 4': 24,
       }
    return switch.get(texte,'Emplacement: ')

#Question Reponse
def QR(etape):
    while etape != 5:
        Audio = question(etape)
        faire_audio(Audio)
        texte = comprehension_audio()
        reponse = reponse_question(etape)
        if texte == reponse:
            ok =1
            print('Reponse juste')
            etape = etape + 1
        else:
            print('Mauvaise reponse')
            mauvais = mauvais + 1
            ok = 0
            if mauvais > 6:
                etape = 5
                print('pb')
    return ok

def ouvrir_porte(emplacement):
    #controle moteur

#Activer file audio
fc.run_all()

#Enregistrement file
fs = 44100  # Sample rate
seconds = 4  # Duration of recording

#Variable connexe
ok = 0
etape = 0

#Debut du main

#Commande pour l'armoire
Audio = question(etape)
faire_audio(Audio)

while True:
    texte = comprehension_audio()
    emplacement = commande(texte)
    etape = 1
    if emplacement != 0:
        #Question/Reponse pour debloquer l'armoire
        ok = QR(etape)
        #Ouverture
        if ok == 1:
            Ouvrir_porte(emplacement)
            print('Porte ouverte')
    if texte == "quitter":
        print("Quitter")
        break
    
#Detection avec phrase contient

##myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
##sd.wait()  # Wait until recording is finished
##write('output.wav', fs, myrecording)  # Save as WAV file
##
##wavefile = 'output.wav'
###WAVFILE = 'racailles.wav'
##decodeSpeech(Wavefile)

###active la transcription de l'enregistrement vocal
##def decodeSpeech(wavefile):
##    r = sr.Recognizer()
##    with sr.WavFile(wavefile) as source:
##        audio = r.record(source)
##        try:
##            print('Transcription GOOGLE: ' + r.recognize_google(
##                audio, language='fr-FR', show_all=False))
##        except LookupError:
##            print('Cannot understand audio!')
## 
##        try:
##            print('Transcription SPHINX: ' + r.recognize_sphinx(
##                audio, language='fr-FR', show_all=False))
##        except sr.UnknownValueError:
##            print('Sphinx could not understand audio')
##        except sr.RequestError as e:
##            print('Sphinx error: {0}'.format(str(e)))
