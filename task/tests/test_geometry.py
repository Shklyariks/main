import pytest

from task.fu.Geometry import circle_perimetr, circle_s

def test_circle_s_1():
    assert circle_s(30) == 30

def test_circle_p_2():
    r = 0
    with pytest.raises(Exception):
        'Это не фигура'

