import numpy as np
import matplotlib.pyplot as plt

def mixedMethod1(x1,mod1):
    a1 = 171
    b1 = 0
    x1 = (a1 * x1 + b1) % mod1
    return x1

def mixedMethod2(x2,mod2):
    a2 = 172
    b2 = 0

    x2 = (a2 * x2 + b2) % mod2
    return x2

def mixedMethod3(x3,mod3):
    a3 = 170
    b3 = 0

    x3 = (a3 * x3 + b3) % mod3
    return x3

def valorU(x1,y1,z1,mod1,mod2,mod3):

    u=((x1/mod1) + (y1/mod2) + (z1/mod3)) % 1
    return u

def listadoAleatorio(cantidad):
    mod1=30269.0
    mod2=30307.0
    mod3=30323.0

    x1 = 15.0
    x2 = 27.0
    x3 = 76.0
    u=[]
    while cantidad>0:
        x1=mixedMethod1(x1,mod1)
        x2=mixedMethod2(x2,mod2)
        x3=mixedMethod3(x3,mod3)
        v=valorU(x1,x2,x3,mod1,mod2,mod3)
                u.append(v)
        cantidad = cantidad-1

    return u

def main():

    cantidad = int(input('cuantas veces desea lanzar los dados: '))

    aleatorios=listadoAleatorio(cantidad)

    x=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    y=1,[2,3,4,5,6,7,8,9]
    acumulada2=[1.0/]
    acumulada=[1.0/36.0,3.0/36.0,6.0/36.0,10.0/36.0,15.0/36.0,21.0/36.0,26.0/36.0,30.0/36.0,33.0/36.0,35.0/36.0,1.0]


    for aleatorio in aleatorios:
        i=0
        for elemento in acumulada:
            if aleatorio <= elemento:
                print x[i],
                break
            i=i+1
    try:
        input('\n\npush enter to finish')
    except:
        print ('finished program')

if __name__ == "__main__":
    main()
