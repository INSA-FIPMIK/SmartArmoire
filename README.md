# SmartArmoire

### Objectif
###### L’objectif du projet est de commander l’ouverture d’une armoire par la voix avec la contrainte de devoir répondre à un questionnaire pour pouvoir déverrouiller l’armoire.

Ce github contient de quoi générer un environnement virtuel sur la Jetson contenant toutes les bibliothèques nécessaires. Les programmes sont dans src, les fichiers autres dans data. 

### Dockerfile
Les instructions pour génerer l'environnement sont sur le github suivant:
#### Created from https://github.com/nlpTRIZ/jetson_docker_X_forwarding
Il faut cependant bien utiliser le fichier dokerfile et le requirement de ce github
### Programme
Le programmme principal s'appelle Programme entier.
Une démonstration pour la partie interaction vocal a été faite sur le fichier Demo_echange_vocal.py

### Sortie PWM
Pour cela il faut dans le terminal de la Jetson exécuter la commande suivante :
sudo /opt/nvidia/jetson-io/jetson-io.py
Cela ouvre les paramètres de configuration de la carte, il faut suivre les étapes suivantes : 
1.	Sélectionner : Configure Jetson 40pin Header 
2.	Sélectionner : Configure Header pins mannually. 
3.	Choisir dans le menu les pin 32 et 33 est les passer en PWM
4.	Enregistrer
5.	Quitter
6.	Rebooter la Jetson nano
Tous les autres fonction et programme sont fait dans le docker_file qui est notre environnement virtuel.

### Fichier audio
Le programme utilise un fichier audio qui permet d'enregistrer, celui-ci se trouve avec le code et doit se nommer enregistrement_audio.wav

### Rapport
Le rapport et la présentation sont disponnible sur ce GitHub
