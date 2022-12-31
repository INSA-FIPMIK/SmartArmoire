#Permet de vérifier l'index des entre/sortie audio et leurs nbr de channel

import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
  dev = p.get_device_info_by_index(i)
  print((i,dev['name'],dev['maxInputChannels'],dev['maxOutputChannels']))
