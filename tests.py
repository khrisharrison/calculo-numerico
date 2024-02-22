import unittest

from biseccion import biseccion
from newton_raphson import newton_raphson

import math

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: (x - 2) ** 2 - math.log(x)
        self.assertEqual(round(biseccion(f,1,2,0.04,5),5),1.40625)
    def test_biseccion2(self):
        f = lambda x: math.e**x - 3 * x ** 2
        self.assertEqual(round(biseccion(f, 0, 1, 0.04, 4), 5), 0.9375)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f = lambda x: (x - 2) ** 2 - math.log(x)
        df = lambda x: 2 * (x - 2) - (1 / x)
        self.assertEqual(round(newton_raphson(1.5,f,df,0.02,4), 5),1.41237)
    def test_newton_raphson2(self):
        f = lambda x: math.e ** x - 3 * x ** 2
        df = lambda x: math.e ** x - 6 * x
        self.assertEqual(round(newton_raphson(0.5, f, df, 0.02, 4), 5), 0.91001)

#class test_riemman(unittest.TestCase):
    #def test_riemman(self):

#class test_trapecio(unittest.TestCase):
    #def test_trapecio(self):

if __name__ == '__main__':
    unittest.main()
