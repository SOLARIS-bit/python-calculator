def add(*args):
    return sum(args)

def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
    
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    try:
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"

