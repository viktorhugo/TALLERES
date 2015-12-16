import numpy as np
import matplotlib.pyplot as plt
from collections import deque

l=int(input('Ingrese la tasa de llegadas: '))
m=int(input('Ingrese la tasa de servicios: '))
t=int(input('Ingrese el numero de tiempos que quiere simular: '))
queed=deque([])
atendidos=deque([])
elemento=1
for i in range(0,t):
    for k in range(0,l):
        queed.append("Elemento "+str(elemento))
        elemento=elemento+1
    for k in range(0,m):
        atendidos.append(queed.popleft())
    print("\nTIEMPO "+str(i+1))
    print("\nqueed")
    for k in range(0,len(queed)):
        print(queed[k])
    print("\nAtendidos")
    for k in range(0,len(atendidos)):
        print(atendidos[k])
print("\nTotal en queed: "+str(len(queed))+" Total atendidos: "+str(len(atendidos)))
