import pyaudio
import wave
import speech_recognition as sr # pip3 install SpeechRecognition
 
chunk = 512      # Each chunk will consist of 1024 samples
sample_format = pyaudio.paInt16      # 16 bits per sample
channels = 2     # Number of audio channels
fs = 44100        # Record at 44100 samples per second
time_in_seconds = 10
filename = "enregistrement_audio.wav"
 
p = pyaudio.PyAudio()  # Create an interface to PortAudio
 
print('-----Now Recording-----')
 
#Open a Stream with the values we just defined
stream = p.open(format=sample_format,
                channels = channels,input_device_index=11,
                rate = fs,
                frames_per_buffer = chunk,
                input = True)

print ("recording...")
frames = []
 

# Initialize array to store frames
 
# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * time_in_seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the Stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
 
print('-----Finished Recording-----')
 
# Open and Set the data of the WAV file
file = wave.open(filename, 'wb')
file.setnchannels(channels)
file.setsampwidth(p.get_sample_size(sample_format))
file.setframerate(fs)
 
#Write and Close the File
file.writeframes(b''.join(frames))
file.close()

filename = 'enregistrement_audio.wav'
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 512 #1024


waveFile = wave.open(filename, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()


audio = pyaudio.PyAudio()
print("audio")
# Open the sound file 
wf = wave.open(filename, 'rb')

print("init")
# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = audio.open(format = FORMAT,
                channels = CHANNELS,
                output_device_index=11,
                rate = RATE,
                frames_per_buffer=CHUNK,
                output = True)

#print("chunk")
# Read data in chunks
data = wf.readframes(CHUNK)

#print("go")
#print(data)
# Play the sound by writing the audio data to the stream

# Play the sound by writing the audio data to the stream
while len(data)>2:
    stream.write(data)
    data = wf.readframes(CHUNK)
    
# Close and terminate the stream
stream.close()
audio.terminate()

rec_vocale = sr.Recognizer()

fichier = "enregistrement_audio.wav", "fr-FR"


with sr.AudioFile("enregistrement_audio.wav") as src: # Ouvre le fichier

    enregistrement = rec_vocale.record(src) # Donne a rec_vocale

    texte = rec_vocale.recognize_google(enregistrement, language=fichier[1]) # Traduction

    print(texte) # Imprime texte

