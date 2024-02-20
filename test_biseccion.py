import pytest
from biseccion import biseccion, f

import math

def test_biseccion():
    assert biseccion(f(1),1,2,0.04,5) == 1.4375