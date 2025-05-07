def add(a, b):
    return a + b


def subtract(a, b):
    # TODO: implement substraction  
    return a - b
    pass


def multiply(a, b):
    # TODO: implement multiplication
    return a * b
    pass


def divide(a, b):
    # TODO: implement this (don't forget to handle division by zero)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    pass
