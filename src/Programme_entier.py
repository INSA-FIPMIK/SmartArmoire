import pyaudio
import wave
import speech_recognition as sr

from Audio import *

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
    SetAudio(num_question)
    PlayAudio(num_question)
    #Enregistrement
    #WAVFILE = 'test3.wav'
    Enregistrer()
    # Test de comprehension fichier audio
    texte = Reco()
    print("fin debut")

def QandR():
    #Debut
    num_question = 1
    while num_question < 5:
        #Emission audio
        SetAudio(num_question)
        PlayAudio(num_question)
        print(num_question)
        #Enregistrement
        Enregistrer()
        # Comprehension audio
        texte = Reco()
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

def ouvrir_porte(emplacement):
    #controle moteur


#Variable connexe
ok = 0
etape = 0

#Debut du main
debut()
#Commande pour l'armoire
Audio = question(etape)
faire_audio(Audio)
ok = QandR()

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
