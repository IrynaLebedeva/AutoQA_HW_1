import pytest

from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square_positive1(simple_math):
    assert simple_math.square(2) == 4

def test_square_positive2(simple_math):
    assert simple_math.square(-3) == 9

def test_square_positive3(simple_math):
    assert simple_math.square(1.2) == 1.44

def test_square_positive4(simple_math):
    assert simple_math.square(-2.5) == 6.25

def test_square_positive5(simple_math):
    assert simple_math.square(0) == 0

def test_cube_positive1(simple_math):
    assert simple_math.cube(2) == 8

def test_cube_positive2(simple_math):
    assert simple_math.cube(-3) == -27

def test_cube_positive3(simple_math):
    assert simple_math.cube(1.2) == 1.728

def test_cube_positive4(simple_math):
    assert simple_math.cube(-2.5) == -15.625

def test_cube_positive5(simple_math):
    assert simple_math.cube(0) == 0


