import numpy as np

def bucle():
    cajas = np.random.permutation(100)

    #print('c =', cajas)

    prisioneros = [False]*len(cajas)

    #print('p =', prisioneros)
    for i in range(0,100):
        j=0
        n=i
        while(j<50):
            if(cajas[n]==i):
                prisioneros[i]=True
                break
            else:
                n=cajas[n]
            j+=1
    return all(prisioneros)

#bucle()
#print('p =', prisioneros)

def simulaciones(s=1000):
    exitos=0
    for i in range(s):
        if bucle():
            exitos+=1
    return exitos/s

print('probabilidad de 1,000 simulaciones = ',simulaciones())
print('probabilidad de 10,000 simulaciones = ',simulaciones(10000))