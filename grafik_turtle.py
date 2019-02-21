import turtle, math
## turtle kan köras objektorienterat aller procedurellt


wn = turtle.Screen()
adam = turtle.Turtle()
bertil = turtle.Turtle()
adam.color('Red')

def spiral1(turt):
    nn=200
    varv=5
    for n in range(nn):
        x=2*math.pi*varv/nn*n
        r=10*x
        turt.goto(r*math.cos(x),r*math.sin(x))



def spiral1(adam):
    nn=200
    varv=5
    for n in range(nn):
        x=2*math.pi*varv/nn*n
        r=10*x
        adam.goto(r*math.cos(x),r*math.sin(x))


def fibonacci(turt,unitstep,nn):
    a=unitstep
    b=a
    for n in range(nn):
        turt.forward(a)
        turt.left(90)
        c=a+b
        a=b
        b=c

fibonacci(bertil,1,20)
    



def grej():
    while True:
        adam.forward(eval(input('Adam framåt: ')))
        bertil.forward(eval(input('Bertil framåt: ')))
        adam.left(eval(input('Adam vänster: ')))
        bertil.left(eval(input('Bertil vänster: ')))
                
