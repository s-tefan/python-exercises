def myeuclides(a,b):
    r=[b]
    q=[]
    while a%b:
        q.append(a//b)
        r.append(a%b)
        a=b
        b=r[-1]
        xx=x[-2]*y[-1]
        yy=x[-1]+y[-1]*y[-2]
    return q,r
