from .main import *

def test_factorial_letter():
    assert factorial_5("a") == "Enter a number equal to or greater than 0"

def test_factorial_four():
    assert factorial_5(4) == 24

def test_factorial_tree():
    assert factorial_5(3) == 6

def test_factorial_two():
    assert factorial_5(2) == 2

def test_factorial_one():
    assert factorial_5(1) == 1

def test_factorial_zero():
    assert factorial_5(0) == 1

def test_factorial_negative():
    assert factorial_5(-1) == "It is impossible to calculate the factorial of a negative number."
