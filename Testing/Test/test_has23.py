import pytest
from Code import has23

def test_has23():
    assert has23.has23([2, 5]) == True
    assert has23.has23([4, 3]) == True
    assert has23.has23([4, 5]) == False
    assert has23.has23([2, 2]) == True
    assert has23.has23([3, 2]) == True
    assert has23.has23([3, 3]) == True
    assert has23.has23([7, 7]) == False
    assert has23.has23([3, 9]) == True
    assert has23.has23([9, 5]) == False
