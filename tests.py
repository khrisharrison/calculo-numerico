import unittest

from biseccion import biseccion
from newton_raphson import newton_raphson
from integracion_riemann import integracion_riemann
from integracion_trapecio import integracion_trapecio

import math

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: (x - 2)**2 - math.log(x)
        self.assertEqual(round(biseccion(f, 1, 2, 0.04, 5), 5),1.40625)
    def test_biseccion2(self):
        f = lambda x: math.e**x - 3 * x**2
        self.assertEqual(round(biseccion(f, 0, 1, 0.04, 4), 5), 0.9375)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f = lambda x: (x - 2)**2 - math.log(x)
        df = lambda x: 2 * (x - 2) - (1 / x)
        self.assertEqual(round(newton_raphson(1.5, f, df, 0.02, 4), 5),1.41237)
    def test_newton_raphson2(self):
        f = lambda x: math.e**x - 3 * x**2
        df = lambda x: math.e**x - 6 * x
        self.assertEqual(round(newton_raphson(0.5, f, df, 0.02, 4), 5), 0.91001)

class test_integracion_riemann(unittest.TestCase):
    def test_integracion_riemann(self):
        f = lambda x: x * (x**2 + 1) ** 0.5
        self.assertEqual(round(integracion_riemann(f, 0, 1, 4), 5), 0.43855)
    def test_integracion_riemann2(self):
        f = lambda x: 3 * x * math.cos(x**2)
        self.assertEqual(round(integracion_riemann(f, 1, 2, 4), 5), -2.00731)

class test_integracion_trapecio(unittest.TestCase):
    def test_integracion_trapecio(self):
        f = lambda x: x * (x**2 + 1) ** 0.5
        self.assertEqual(round(integracion_trapecio(f, 0, 1, 4), 5), 0.61533)
    def test_integracion_trapecio2(self):
        f = lambda x: 3 * x * math.cos(x**2)
        self.assertEqual(round(integracion_trapecio(f, 1, 2, 4), 5), -2.29493)

if __name__ == '__main__':
    unittest.main()
