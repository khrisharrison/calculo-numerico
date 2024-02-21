import math

def biseccion(f,a,b,E,Ni):

    E_aprox = 1 #error aproximado
    i = 0 #contador del numero de iteraciones
    m_actual = 0 #Punto medio actual
    m_anterior = 0 #Punto medio anterior

    while i < Ni  and E_aprox > E:
        m_anterior = m_actual
        m_actual = (a + b)/2
        if f(m_actual) * f(b) < 0:
            a = m_actual
        else:
            b = m_actual

        if i >= 1:
            E_aprox = abs((m_actual - m_anterior) / m_actual)

        i += 1

    print("Error:",E_aprox)
    print("Numero de Iteraciones:",i)

    return m_actual

if __name__ == "__main__":
    f = lambda x: (x-2)**2 - math.log(x) #funcion
    a = 1 #intervalo a
    b = 2 #intervalo b
    E = 0.04 #tolerancia de error
    Ni = 5 #numero de intentos
    print("Punto medio aproximado:",biseccion(f, a, b, E, Ni))