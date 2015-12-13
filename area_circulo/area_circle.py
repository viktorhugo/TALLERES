import matplotlib.pyplot as plt
import numpy as np

def random(x1,x2,x3,escala,cantidad):
    V1 = 180.0
    X1 = 10.0
    v2 = 182.0
    x2 = 10.0
    z3 = 180.0
    j3 = 10.0
    modulo_a=37269.0
    modulo_b=37307.0
    modulo_c=37323.0

    x=[]

    for n in range(0,cantidad):
        x1 = (V1 * x1 + X1) % modulo_a
        x2 = (v2 * x2 + x2) % modulo_b
        x3 = (z3 * x3 + j3) % modulo_c
        v = ((x1/modulo_a) + (x2/modulo_b) + (x3/modulo_c)) %1

        v=(2*escala*v)-escala

        x.append(v)


    return x


def circulo(r,phi):
    return r*np.cos(phi), r*np.sin(phi)




def main():
    radio=5.0#float(input('radio del circulo: '))
    puntos=10000#float(input('cantidad de puntos aleatorios: '))
    semilla1=26
    semillv2=62
    semillz3=98

    x=random(semilla1,semillv2,semillz3,radio,puntos) # 3 semillas y cantidad de datos
    y=random(semillz3,semilla1,semillv2,radio,puntos)

    dx=[]
    dy=[]

    fx=[]
    fy=[]

    i=0
    for point in x:
        isin= (x[i]**2) + (y[i]**2)
        if( (isin) <= (radio**2) ):
            dx.append(x[i])
            dy.append(y[i])
        else:
            fx.append(x[i])
            fy.append(y[i])

        i=i+1

    print (dx)
    print (fx)


    area=(radio**2)*np.pi
    estimada=((2*radio)**2)*(float(len(dx))/float(puntos))
    error=area-estimada



    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')

    phis=np.arange(0,6.28,0.01)
    ax.plot( *circulo(radio,phis), c='k',ls='-' )
    ax.scatter(dx,dy,label='adentro', color='b', marker='o', s=2)
    ax.scatter(fx,fy,label='afuera', color='r', marker='o', s=2)
    plt.title('Area de un circulo\n Area real:'+str(area)+' Area estimada: '+str(estimada)+' Error: '+str(error))

    plt.show()


    try:
        input('press something to finish')
    except:
        print ('finished program')


if __name__ == "__main__":
    main()
