import math

def integracion_riemann(f,a,b,n):
    h = (b - a) / n
    acum = 0
    x = a
    for i in range(n):
        acum = acum + h * f(x)
        x = x + h
    return acum

if __name__ == "__main__":
    f = lambda x: x*(x**2+1)**0.5
    a = 0
    b = 1
    n = 4
    print("Valor Aproximado:",integracion_riemann(f,a,b,n))