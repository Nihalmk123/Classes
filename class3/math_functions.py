#math function library

#function for addition
def add(a, b):
    return a + b

#function for substraction
def subtract(a, b):
    return a - b

#function for multipllication
def multiply(a, b):
    return a * b

#function for division
def divide(a, b):
    return a / b
    
#function for exponentiate
def exponentiate(a, b):
    return a ** b

# Specify functions to export
__all__ = ['add', 'subtract', 'multiply', 'divide', 'exponentiate']
