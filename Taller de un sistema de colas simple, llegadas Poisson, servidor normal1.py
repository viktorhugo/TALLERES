import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def main():
    la=5
    mu=3
    si=2
    l=np.random.poisson(la)
    m=np.random.uniform(mu,si)
    ts=2 #Tiempo que dura en el sistema
    num_iteraciones=3
    cola=deque([])
    sistema=deque([])
    atendidos=deque([])
    elemento=1
    for i in range(0,num_iteraciones):
        l=int(np.random.poisson(la))
        m=int(np.random.uniform(mu,si))
        for k in range(1,l+1):
            cola.append("Elemento "+str(elemento))
            elemento=elemento+1
        for k in range(1,m+1):
            sistema.append(cola.popleft())
        if(i%ts==0):
            for k in range(1,m+1):
                atendidos.append(sistema.popleft())
        print("\nl: "+str(l)+" m:"+str(m)+" cola: "+str(len(cola))+" sistema: "+str(len(sistema))+" atendidos: "+str(len(atendidos)))
        print("\nCola")
        for k in range(0,len(cola)):
            print(cola[k])
        print("\nSistema")
        for k in range(0,len(sistema)):
            print(sistema[k])
        print("\nAtendidos")
        for k in range(0,len(atendidos)):
            print(atendidos[k])

if __name__ == "__main__":
    main()
