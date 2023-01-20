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
       0: Debut_enregistrement,
       1: Bienvenu,
       2: Question1,
       3: Question2,
       4: Question3,
       5: Question4,
       6: Final,
       }
    return switch.get(num_question)

def reponse_question(reponse):
    switch={
       0: 'Bonjour',
       1: 'truc',
       2: 'singe',
       3: 'rep3',
       4: 'rep1',
       5: 'merci',
       }
    return switch.get(num_question)

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

def texte_cmd(texte):
    if ('droite' and 'haut') in texte:
        print("Correct")
        cmd = 3
    elif ('droite' and 'bas') in texte:
        print("Correct")
        cmd = 4
    elif ('gauche' and 'haut') in texte:
        print("Correct")
        cmd = 5
    elif ('gauche' and 'bas') in texte:
        print("Correct")
        cmd = 6
    elif 'repeter' in texte:
        print("repeter")
        cmd = 1
        cmd = debut()
    elif 'quitter' in texte:
        print("quitter")
        cmd = 2
    else:
        print("Faux")
        cmd = 0
    return cmd

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
    cmdPorte = texte_cmd(texte)
    print("fin debut")
    return cmdPorte

def QandR():
    #Debut
    num_question = 2
    while num_question < 6:
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

def Verif_Ouverture():
    if capteur == 1:
        ok = QandR()
    else:
        ok = 0   
    return ok

def cmd_MoteurOuvre(cmdPorte):
    #ouverture selon cmdPorte

def cmd_MoteurFerme(cmdPorte):
    #fermeture selon cmdPorte

#Variable connexe
ok = 0
etape = 0

#Attente pression bouton
while bouton == 1:
    #attente

#lancement programme
cmdPorte = debut()
if cmdPorte =! 0:
    #Si pas quitter
    ok = Verif_Ouverture()
    if ok ==1:
        print("ouverture")
        cmd_MoteurOuvre(cmdPorte)
        while capteur == 1:
            #attente enlever tiroir
        print("fermeture")
        cmd_MoteurFerme(cmdPorte)
