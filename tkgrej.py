import tkinter as tk
import math
#from math import *

root = tk.Tk()
c = tk.Canvas(root, width = 400, height = 400, bg = "blue")
line = c.create_line(10,10,20,50,50,50, fill = "red" )
c.pack
root.mainloop()
