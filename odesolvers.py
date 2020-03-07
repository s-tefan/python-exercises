import math

def euler(fun,t_list,y0):
    y=[y0]
    for k in range(len(t_list)-1):
        t = t_list[k]
        dt = t_list[k+1]-t
        dy = fun(t,y[-1])*dt
        y.append(y[-1]+dy)
    return y

t_list = [k/16 for k in range(17)]
y = euler((lambda t,y: -y), t_list, 1 )
print(y)
print(list(math.exp(-t) for t in t_list))






