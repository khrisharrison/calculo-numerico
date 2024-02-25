def integracion_trapecio(f, a, b, n):
    h = (b - a) / n # tamaño de cada subintervalo
    acum = 0
    xi = a #xi
    xi1 = a + h #xi+1
    for i in range(n):
        acum = acum + ((f(xi) + f(xi1)) * h) / 2 #se aplica la formula del metodo del trapecio
        xi += h # se le incrementa a xi el valor de h
        xi1 += h # se le incrementa a xi+1 el valor de h
    return acum

if __name__ == "__main__":
    f = lambda x: x * (x**2 + 1) ** 0.5 # funcion f(xi)
    a = 0 # intervalo a
    b = 1 # intervalo b
    n = 4 # numero de subintervalos
    print("Valor Aproximado:", integracion_trapecio(f, a, b, n))