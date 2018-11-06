print("Ge utetemperatur i grader celsius: ")
temperatur=float(input())
if temperatur < 5:
    print("Burr, idag är det kallt!")
elif temperatur <15:
    print("Idag är det svalt!")
elif temperatur <25:
    print("Skönt väder idag!")
else:
    print("Fy f*n vad hett!")
