def add(*args):
    return sum(args)

def subtract(*args):
    """Subtract an unlimited number of numbers."""
    print("Executing improved subtract function...")
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

