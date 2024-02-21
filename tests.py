import unittest

from biseccion import biseccion

import math

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: (x - 2) ** 2 - math.log(x)
        self.assertEqual(round(biseccion(f,1,2,0.04,5),5),1.40625)


if __name__ == '__main__':
    unittest.main()
