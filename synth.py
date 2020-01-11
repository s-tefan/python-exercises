import math
import pyaudio

pa = pyaudio.PyAudio()
br = 16000

class Envelope:
    def __init__(self, attack, decay, release, sustainlevel = 0.5):
        self.attack = attack # attack in seconds
        self.decay = decay # decay in seconds
        self.release = release # release in seconds
        self.sustainlevel = sustainlevel # sustain level relative to attack level
    def parameters(self):
        return attack, decay, release, sustainlevel


def sine(duration, frequency, env, bitrate):
    w = []
    for ts in range(duration*bitrate):
        k = 2*math.pi*frequency/bitrate
        si = math.sin(k*ts)
        a,d,r,sl = env.parameters()
        if ts <= a*bitrate:
            x = si/(a*bitrate)
        elif ts <= (a+d)*bitrate:
            x = 1 + (si - a)*(sl - 1)/d
        elif ts <= duration - r:
            x = sl
        else:
            x = (ts - duration)*(-sl)/r
        w.append(x)
    return w

stream = pa.open(format = pa.get_format_from_width(1), 
                channels = 1, 
                rate = br, 
                output = True)

env = Envelope(0.05,0.2,0.1,0.5)
wave = sine(1,440,env,br)
stream.write(wave)
stream.stop_stream()
stream.close()
pa.terminate()