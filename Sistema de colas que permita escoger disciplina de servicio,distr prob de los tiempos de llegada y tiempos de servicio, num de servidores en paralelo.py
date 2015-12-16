import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

dl=int(input('Digite la distribucion del tiempo de llegada (1. Exponencial 2. Deterministica 3. Erlang 4. Arbitraria): '))
dm=int(input('Digite la distribucion del tiempo de servicio (1. Exponencial 2. Deterministica 3. Erlang 4. Arbitraria): '))
s=int(input('Ingrese el numero de servidores en paralelo: '))
d=int(input('Digite la disciplina de la queed (1. FIFO 2. LIFO 3. SIRO): '))
t=int(input('Ingrese el numero de tiempos que quiere simular: '))
ll=int(input('Ingrese tamano de la fuente de entrada: '))
mm=int(input('Ingrese la capacidad de un servidor: '))
queed=deque([])
atendidos=deque([])
elemento=1
for i in range(0,t):
    if(dl==1):
        l=random.expovariate(ll)
    if(dl==2):
        l=ll
    if(dl==3):
        l=random.gammavariate(ll,t+1)
    if(dl==4):
        l=random.randrange(ll)
    if(dm==1):
        m=random.expovariate(mm)
    if(dm==2):
        m=mm
    if(dm==3):
        m=random.gammavariate(mm,t+1)
    if(dm==4):
        m=random.randrange(mm)
    l=int(l)
    m=int(m)
    for k in range(0,l):
        queed.append("Elemento "+str(elemento))
        elemento=elemento+1
    for k in range(0,m*s):
        if(d==1):
            atendidos.append(queed.popleft())
        if(d==2):
            atendidos.append(queed.pop())
        if(d==3):
            valor=random.choice(queed)
            atendidos.remove(valor)
    print("\nTIEMPO "+str(i+1))
    print("\nqueed")
    for k in range(0,len(queed)):
        print(queed[k])
    print("\nAtendidos")
    for k in range(0,len(atendidos)):
        print(atendidos[k])
print("\nTotal en queed: "+str(len(queed))+" Total atendidos: "+str(len(atendidos)))
