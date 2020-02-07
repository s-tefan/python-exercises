import scipy.integrate as si
import matplotlib.pyplot as plt

def ydot(t,y):
    return -y**2

t_span = [0,4]
y0 = [1]
sol = si.solve_ivp(ydot, t_span, y0)
print(sol.t, sol.y)

p = plt.plot(sol.t,sol.y[0])

plt.show()
