def integracion_riemann(f, a, b, n):
    h = (b - a) / n # tamaño de cada subintervalo
    acum = 0
    x = a + h #x1
    for i in range(n-1):
        acum = acum + h * f(x) #se aplica la formula del metodo de Riemann
        x += h # se le incrementa a x el valor de h
    return acum

if __name__ == "__main__":
    f = lambda x: x * (x**2 + 1) ** 0.5  # funcion f(xi)
    a = 0  # intervalo a
    b = 1  # intervalo b
    n = 4  # numero de subintervalos
    print("Valor Aproximado:", integracion_riemann(f, a, b, n))