import math

def biseccion(f, a, b, Er, Num_i):

    E_aprox = 1 #error aproximado
    i = 0 #contador del numero de iteraciones
    pm_actual = 0 #Punto medio actual
    pm_anterior = 0 #Punto medio anterior

    while i < Num_i and E_aprox > Er:
        pm_anterior = pm_actual
        pm_actual = (a + b) / 2
        if f(pm_actual) * f(b) < 0:
            a = pm_actual
        else:
            b = pm_actual

        if i >= 1:
            E_aprox = abs((pm_actual - pm_anterior) / pm_actual)

        i += 1

    print("Error:",E_aprox)
    print("Numero de Iteraciones:", i)

    return pm_actual

if __name__ == "__main__":
    f = lambda x: (x-2)**2 - math.log(x) #funcion f
    a = 1 #intervalo a
    b = 2 #intervalo b
    E = 0.04 #tolerancia de error
    Ni = 5 #numero de intentos
    print("Punto medio aproximado:",biseccion(f, a, b, E, Ni))