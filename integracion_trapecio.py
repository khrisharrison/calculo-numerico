def integracion_trapecio(f, a, b, n):
    h = (b - a) / n # tamaño de cada subintervalo
    acum = 0
    x = a
    xi = a + h
    for i in range(n):
        acum = acum + ((f(x) + f(xi)) * h) / 2
        x = x + h
        xi = xi + h
    return acum

if __name__ == "__main__":
    f = lambda x: x * (x**2 + 1) ** 0.5 # funcion
    a = 0 # intervalo a
    b = 1 # intervalo b
    n = 4 # numero de subintervalos
    print("Valor Aproximado:", integracion_trapecio(f, a, b, n))