import pyglet
import time
from pyglet.window import mouse
import math

# global variables
g_tick = 0

win = pyglet.window.Window()




adsr = pyglet.media.synthesis.ADSREnvelope(0.05, 0.2, 0.1)

saw = pyglet.media.synthesis.Sawtooth(duration=0.1, frequency=220, envelope=adsr)
fm = pyglet.media.synthesis.FM(0.5, carrier=440, modulator=2, mod_index=22, envelope=adsr)

def majorscale(key_freq):
    scale = [1,9/8,5/4,4/3,3/2,5/3,15/8,2]
    for volta in [1]:
        for k in scale:
            print(k,k*key_freq)
            yield pyglet.media.synthesis.FM(
                duration=0.5, 
                carrier=k*key_freq, 
                modulator = 3*k*key_freq,
                mod_index = 2,
                envelope=adsr)

player = pyglet.media.Player()
#saw.play()
#fm.play()
#player.queue(saw)
#player.queue(fm)
player.loop = False
scale = majorscale(220)
#scalelist = list(scale)
#print(scalelist)
sg = pyglet.media.SourceGroup()
#player.queue(scale)

for note in scale:
    player.queue(note)
    sg.add(note)
    #player.play()
    #time.sleep(0.5)
    #player.pause()
player.queue(sg)
'''
player.queue(pyglet.media.synthesis.FM(
    1,
    carrier = 220,
    modulator = 10,
    envelope = adsr)
)
'''
'''
scale = [1,9/8,5/4,4/3,3/2,5/3,15/8,2]
scale_freq = [pyglet.media.synthesis.Sawtooth(
    0.2,
    frequency = 220*note,
    envelope = adsr) for note in scale]
player.queue(scale_freq)
scale_freq = [pyglet.media.synthesis.FM(
    1,
    carrier = 220*note,
    modulator = 5,
    mod_index = 0.2,
    envelope = adsr) for note in scale]
player.queue(scale_freq)
'''
player.play()


pyglet.app.run()
