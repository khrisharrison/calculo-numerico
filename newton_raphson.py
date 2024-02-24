import math

def newton_raphson(xi, f, df, Er, Num_i):
    E_aprox = 1 #error aproximado
    i = 0 #contador del numero de iteraciones
    xi1 = 0 #punto xi+1

    while i < Num_i and E_aprox > Er:
        xi1 = xi - f(xi) / df(xi)
        if i >= 1:
            E_aprox = abs(xi - xi1)
        xi = xi1

        i += 1

    print("Error:", E_aprox)
    print("Numero de Iteraciones:", i)

    return xi1

if __name__ == "__main__":
    f = lambda x: (x-2)**2 - math.log(x) #funcion f
    df = lambda x: 2*(x-2) - (1/x) #derivada de f
    x0 = 1.5 #valor inicial de X
    E = 0.02 #tolerancia de error
    Ni = 4 #numero de iteraciones
    print("xi+1:", newton_raphson(x0, f, df, E, Ni))