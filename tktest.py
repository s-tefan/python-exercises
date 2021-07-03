import tkinter as tk
import random
from math import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        relieftype="groove"
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["relief"] = relieftype
        self.hi_there["command"] = self.say_hi

        self.fentry=tk.StringVar(); self.fentry.set('x')
        self.canv = tk.Canvas(self,height=300,width=300)
        self.functionentry = tk.Entry(self, textvariable=self.fentry)
        self.functionentry.bind("<KeyRelease-Return>",self.eret)
        self.randline = tk.Button(self)
        self.randline["text"] = "Plot!"
        self.randline["relief"] = relieftype
        self.randline["command"] = self.plotentry #self.draw
        self.quit = tk.Button(self, text="QUIT", fg="red", relief = relieftype,
                              command=self.master.destroy)

        self.canv.grid(row=0,column=0,columnspan=2)
        self.functionentry.grid(row=1,column=0)
        self.randline.grid(row=1,column=1)
        self.hi_there.grid(row=2,column=0)
        self.quit.grid(row=2,column=1)



    def say_hi(self):
        print("hi there, everyone!")

    def draw(self):
        xlist,ylist=[],[]
        for k in range(10):
            xlist.append(random.randrange(0,xres))
            ylist.append(random.randrange(0,yres))
#        myline=self.canv.create_line(x1,y1,x2,y2)
        myline=self.drawgraph(self.canv,xlist,ylist)


    def drawgraph(self,canvas,xcoordlist,ycoordlist):
        l=[]
        for k in range(len(xcoordlist)):
            l.append(xcoordlist[k])
            l.append(ycoordlist[k])
        graph=canvas.create_line(*l)


    def plot(self,funk):
        xres,yres=self.canv.winfo_width()-3,self.canv.winfo_height()-3
        print("plot",funk)
        xlist=[k/xres for k in range(xres)]
#        yccordlist=[eval(funk) for x in xcoordlist]
        ylist=[eval(funk) for x in xlist]
        xcoordlist=[x*xres for x in xlist]
        ycoordlist=[yres-y*yres for y in ylist]
        ml=self.drawgraph(self.canv,xcoordlist,ycoordlist)
    def plotentry(self):
        self.plot(self.fentry.get())
    def eret(self,event):
        self.plotentry()

root = tk.Tk()
app = Application(master=root)


app.mainloop()
