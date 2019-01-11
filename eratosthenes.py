nl=list(range(2,10000))
pl=[]
while nl:
    p=nl.pop(0)
    pl.append(p)
    for k in range(len(nl)):
        if nl[k]%p==0:
            nl[k]=0
    nl=[x for x in nl if x!=0]
    
        
            

            
