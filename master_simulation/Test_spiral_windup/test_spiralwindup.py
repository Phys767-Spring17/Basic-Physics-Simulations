from spiralwindup import vel
import math
import pytest

max = 1.4*5*math.exp(-5.0/20.0)
min = 5.0
m = (max - min)/(-1.0)

def test_spiral_windup_1():
    assert vel(2.0) == 1.4*2.0*math.exp(-2.0/20.0) #this should be true

def test_spiral_windup_2():
    assert vel(-2.0) == 1.4*2.0*math.exp(-2.0/20.0) #this should be true

def test_spiral_windup_3():
    assert vel(-2.0) == 1.4*-2.0*math.exp(2.0/20.0) #this should be false b/c ar gives the absolute value of r

def test_spiral_windup_4():
    assert vel(5.1) == 1.4*5.1*math.exp(-5.1/20.0) #this should be false b/c ar > 5

def test_spiral_windup_5():
    assert vel(5.1) == m*(5.1 - 5.0) + max #this should be true

def test_spiral_windup_6():
    assert vel(7.0) == 5.0 #this should be true
