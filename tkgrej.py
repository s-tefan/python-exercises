import tkinter as tk
import math
#from math import *

def greja():
    c.coords(line,10,10,20,40,50,60)


root = tk.Tk()
c = tk.Canvas(root, width = 400, height = 400, bg = "blue")
b = tk.Button(root,text="Greja!", fg="red", 
                              command = greja)
line = c.create_line(10,10,20,50,50,50, fill = "red")
print(line)
c.pack()
b.pack()




root.mainloop()
