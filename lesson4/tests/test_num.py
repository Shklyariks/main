from lesson4.lesson4_1 import num_1
import pytest

def test_num_1():
    assert num_1(2022, 2) == 28

def test_num_2():
    with pytest.raises(Exception):
        num_1()


