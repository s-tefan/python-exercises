import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
#p.terminate()
'''Gör inget med det inspelade. Nästa steg att spela upp.'''

outstream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

# play stream (3)
for chunk in frames:
    outstream.write(chunk)

# stop stream (4)
outstream.stop_stream()
outstream.close()

# close PyAudio (5)
p.terminate()
