def integracion_riemann(f, a, b, n):
    h = (b - a) / n # tamaño de cada subintervalo
    acum = 0
    x = a
    for i in range(n):
        acum = acum + h * f(x)
        x = x + h
    return acum

if __name__ == "__main__":
    f = lambda x: x * (x**2 + 1) ** 0.5  # funcion
    a = 0  # intervalo a
    b = 1  # intervalo b
    n = 4  # numero de subintervalos
    print("Valor Aproximado:",integracion_riemann(f, a, b, n))