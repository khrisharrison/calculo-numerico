import math

def biseccion(f,a,b,E,Ni):

    Ea = 1 #error aproximado
    i = 1 #contador del numero de iteraciones
    m_actual = 0 #Punto medio actual
    m_anterior = 0 #Punto medio anterior

    while i < Ni  and Ea > E:
        m_anterior = m_actual
        m_actual = (a + b)/2
        if f(m_actual) * f(b) < 0:

            a = m_actual
        else:
            b = m_actual

        if i >= 1:
            Ea = abs((m_actual - m_anterior) / m_actual)

        i += 1

    print(m_actual)
    print(Ea)
    print(i)

    return m_actual

def f(x):
    return (x-2)**2 - math.log(x)
a = 1
b = 2
E = 0.04
Ni = 5
m = biseccion(f, a, b, E, Ni)