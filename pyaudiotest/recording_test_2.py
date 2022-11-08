import pyaudio
import wave

#CHUNK = 1024
CHUNK = 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

instream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

outstream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

print("* recording")


# Läs in ljuddata i bytesform och lagra i en lista frames 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = instream.read(CHUNK)
    outstream.write(data)


print("* done recording")



# stop streams (4)
instream.stop_stream()
instream.close()
outstream.stop_stream()
outstream.close()

# close PyAudio (5)
p.terminate()
