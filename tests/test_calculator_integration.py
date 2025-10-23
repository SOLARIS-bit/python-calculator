import pytest

from src.calculator import run_operation
from src.utils import divide

def test_add():
    assert run_operation("1", 3, 4) == 7

def test_subtract():
    assert run_operation("2", 10, 4) == 6

def test_multiply():
    assert run_operation("3", 3, 5) == 15

def test_divide():
    assert run_operation("4", 12, 3) == 4

def test_divide_by_zero():
    # Vérifie le comportement réel de divide(a,0)
    result = divide(5, 0)
    assert result == "Error: Division by zero"

def test_invalid_choice():
    with pytest.raises(ValueError):
        run_operation("9", 1, 1)

