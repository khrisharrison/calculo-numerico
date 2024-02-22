import unittest

from biseccion import biseccion
from newton_raphson import newton_raphson

import math

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: (x - 2) ** 2 - math.log(x)
        self.assertEqual(round(biseccion(f,1,2,0.04,5),5),1.40625)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f = lambda x: (x - 2) ** 2 - math.log(x)
        df = lambda x: 2 * (x - 2) - (1 / x)
        self.assertEqual(round(newton_raphson(1.5,f,df,0.02,4), 5),1.41237)

if __name__ == '__main__':
    unittest.main()
