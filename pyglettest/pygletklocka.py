import pyglet
from pyglet.window import mouse
import math
import copy

# global variables
g_tick = 0

win = pyglet.window.Window()


square = pyglet.graphics.vertex_list(
    4,
    ("v2f", [0, 100, 10, 100, 10, 110, 0, 110]),
    ("c3B", (255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 255)),
)

visare = pyglet.graphics.vertex_list(
    3, ("v2f", [0, 100, 5, 0, -5, 0]), ("c3B", (255, 0, 0, 255, 0, 0, 255, 0, 0))
)

# visare_shape = pyglet.shapes.Triangle(\
#        0,100, 5,0, -5,0, \
#        color = (255,0,0))
def make_visare():
    visare_shape = pyglet.shapes.Polygon(
        [0, 0],
        [5, 0],
        [0, -5],
        [-5, 0],
        [0, 100],
    )
    # visare_shape.anchor_position = (0,0)
    return visare_shape


sekundvisare = make_visare()
minutvisare = make_visare()
minutvisare.color = (255, 255, 255)


@win.event
def on_draw():
    win.clear()
    minutvisare.draw()
    sekundvisare.draw()


@win.event
def move_it(dt):
    global g_tick
    r = 100
    g_tick += 1
    c = 1
    d = math.pi / 180  # en grad i taget
    s = d * 6
    sekundvisare.rotation = s * g_tick
    minutvisare.rotation = 10 * s * g_tick


pyglet.clock.schedule_interval(move_it, 1 / 60)


pyglet.app.run()
