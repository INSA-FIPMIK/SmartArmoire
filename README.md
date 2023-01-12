# SmartArmoire
## Created from https://github.com/nlpTRIZ/jetson_docker_X_forwarding
### Objectif
###### L’objectif du projet est de commander l’ouverture d’une armoire par la voix avec la contrainte de devoir répondre à un questionnaire pour pouvoir déverrouiller l’armoire.
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
### Rapport
