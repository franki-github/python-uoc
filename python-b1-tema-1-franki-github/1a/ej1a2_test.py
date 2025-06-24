from ej1a2 import sum_odd_numbers
import pytest

def test_sum_odd_numbers():
    assert sum_odd_numbers([1,2,3,4,5]) == 9, "sum_odd_numbers does not return the correct value for [1,2,3,4,5]. It should be 9"
    assert sum_odd_numbers([2,4,6,8,10]) == 0, "sum_odd_numbers does not return the correct value for [2,4,6,8,10]. It should be 0"
    assert sum_odd_numbers([1,3,5,7,9]) == 25, "sum_odd_numbers does not return the correct value for [1,3,5,7,9]. It should be 25"


