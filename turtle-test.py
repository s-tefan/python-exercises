import turtle, math


def polygon(turt,sideno,sidelength):
    """Ritar en polygon med sideno sidor av längd sidelength."""
    for n in range(sideno):
        turt.fd(sidelength)
        turt.lt(360/sideno)

def polygon_r(turt,sideno,radius):
    sidelength=2*math.pi*radius/sideno
    polygon(turt,sidelength,sideno)


def polyline(t, n, length, angle): # Från Think Python
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(turt,sidelength,sideno): #Refactoring polygon to use arc
    """Ritar en polygon med sideno sidor av längd sidelength, genom att använda polyline"""
    polyline(turt,sideno,sidelength,360/sideno)

def arc(t, r, angle): # Från Think Python
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    


print(polygon.__doc__)

bob = turtle.Turtle()
##
##bob.fd(100)
##bob.lt(90)
##bob.fd(100)
### print(bob)
##for k in range(3,7):
##    polygon_r(bob,k,100)
##    # Kommer den gamla eller nya definitionen av polygon att användas?
##    # Svaret är den nya, då den definierar om vilken funktion som har namnet polygon
##    # Detta trots att polygon_r definierats innan polygon definierats om.

##bob.pencolor("Red")
##v=36
##w=180-v
##l=100
##bob.lt(v)
##for k in range(5):
##    bob.fd(l)
##    bob.lt(w)
##bob.rt(v)

def ngram(t,length,n,k):
    w=360*k/n
    for k in range(n):
        bob.fd(l)
        bob.lt(w)

def ngram_r(t,radius,n,k):
    w=360*k/n
    v=90+k*180/n
    wasdown=t.isdown()
    t.penup()
    t.fd(radius) # startar från centrum
    t.lt(v)
    t.pendown()
    l=2*radius*math.sin(math.pi/360*w)
    for k in range(n):
        t.fd(l)
        t.lt(w)
    t.penup()
    t.rt(v)
    t.bk(radius)
    if wasdown:
        t.pendown()


bob.speed(6)
bob.pencolor("Blue")
#ngram_r(bob,200,7,3)
ngram_r(bob,200,17,6)

bob.speed(9)    
bob.pencolor("Magenta")
ngram_r(bob,200,17,8)

bob.pencolor("Green")
ngram_r(bob,200,17,7)
 
bob.speed(0)
bob.pencolor("Pink")
ngram_r(bob,200,53,1)
 


    
turtle.mainloop()
