from ej1a1 import fibonacci
import pytest

def test_fibonacci_():
    assert fibonacci(0) == 0, "fibonacci does not return the correct value for input 0. It should be 0"
    assert fibonacci(1) == 1, "fibonacci does not return the correct value for input 1. It should be 1"
    assert fibonacci(6) == 8, "fibonacci does not return the correct value for input 6. It should be 8"
    assert fibonacci(10) == 55, "fibonacci does not return the correct value for input 10. It should be 55"

