def add(*args):
    """Add an unlimited number of numbers."""
    print("Executing improved add function...")
    return sum(args)


def subtract(*args):
    """Subtract an unlimited number of numbers."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    """Multiply an unlimited number of numbers."""
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    """Divide sequentially all provided numbers."""
    try:
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
