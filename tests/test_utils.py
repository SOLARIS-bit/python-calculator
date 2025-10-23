from src.utils import add, subtract, multiply, divide


def test_add():
    assert add(1, 2, 3) == 6
    assert add() == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(10, 3, 2) == 5
    assert subtract() == 0


def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(5) == 5
    assert multiply() == 1


def test_divide():
    assert divide(10, 2) == 5
    assert divide(8, 2, 2) == 2
    assert divide(10, 0) == "Error: Division by zero"
