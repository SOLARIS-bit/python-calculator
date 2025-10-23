# src/calculator.py
from src.utils import add, subtract, multiply, divide

def run_operation(choice, a, b):
    if choice == "1":
        return add(a, b)
    elif choice == "2":
        return subtract(a, b)
    elif choice == "3":
        return multiply(a, b)
    elif choice == "4":
        return divide(a, b)
    else:
        raise ValueError("Invalid choice")
