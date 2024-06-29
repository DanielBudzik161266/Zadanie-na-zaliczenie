# program2.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def power(a, b):
    return a ** b

print(add(3, 4))
print(subtract(7, 2))
print(multiply(3, 5))
print(divide(10, 2))
print(divide(10, 0))
print(power(2, 3))

