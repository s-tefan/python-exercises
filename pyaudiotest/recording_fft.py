import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

#CHUNK = 1024
CHUNK = 11025
FORMAT = pyaudio.paInt16
CHANNELS = 1
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
    int_data = list(int.from_bytes(data[2*k:2*k+2], 'little', signed = True) for k in range(len(data)//2))
    if i == 3: 
        n = len(int_data)
        fft_data = np.fft.fft(int_data) / n
        fft_fix = [abs(fft_data[k]*fft_data[n-k]) for k in range(1,n//2)]
        print(int_data, fft_data, fft_fix)
        m = 1000
        x = list(range(m))
        fig, ax = plt.subplots()
        ax.plot(x,np.log10(fft_fix[:m]))
        plt.show()
    outstream.write(data)


print("* done recording")



# stop streams (4)
instream.stop_stream()
instream.close()
outstream.stop_stream()
outstream.close()

# close PyAudio (5)
p.terminate()
