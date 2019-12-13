import pyglet
from pyglet.window import mouse
import math

# global variables
g_tick = 0

win = pyglet.window.Window()


square = pyglet.graphics.vertex_list(4, \
        ('v2f',[0,100, 10,100, 10,110, 0,110]), \
        ('c3B',(255,0,0, 255,0,0, 255,0,0, 0,0,255)))

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=win.width//2, y=win.height//2,
                          anchor_x='center', anchor_y='center')

@win.event
def on_draw():
        win.clear()
        label.draw()
        square.draw(pyglet.gl.GL_POLYGON)

@win.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
       for k in range(4):
                square.vertices[2*k] +=  dx
                square.vertices[2*k+1] +=  dy
       

def move_it(dt):
        global g_tick
        r = 100
        g_tick += 1
        c = 1
        d = math.pi/180 # en grad i taget
        for k in range(4):
                square.vertices[2*k] += c * math.sin(d*g_tick)
                square.vertices[2*k+1] += c * math.cos(d*g_tick)

pyglet.clock.schedule_interval(move_it, 1/60)


 
pyglet.app.run()
