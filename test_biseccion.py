import pytest
from biseccion import biseccion

import math

def test_biseccion():
    f = lambda x: (x - 2) ** 2 - math.log(x)
    assert round(biseccion(f,1,2,0.04,5),5) == round(1.40625,5)