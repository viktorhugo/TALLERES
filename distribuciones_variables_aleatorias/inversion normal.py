import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

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

def random_list(cantidad):
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

from scipy.integrate import quad


def integrand(t,x):
    return np.exp(-(t**2))


def invErrorFunction(x):
    I = quad(integrand, 0, x, args=(x))[0]
    resultado= (2/np.sqrt(np.pi))*(1/I)


    return resultado



def normal_inversa(cantidad,media,varianza):
    aleatorios=random_list(cantidad)

    valor=0.0
    resultado=[]
    for x in range(cantidad):
        valor= media + (varianza * np.sqrt(2)*invErrorFunction(2*aleatorios[x]-1))
        resultado.append(valor)

    return resultado



def main():

    cantidad = 10
    media=0.0
    varianza= 1.0

    resultado=[]
    resultado=normal_inversa(cantidad, media, varianza)
    print (resultado)



    try:
        input('\n\npush enter to finish')
    except:
        print ('finished program')

if __name__ == "__main__":
    main()
