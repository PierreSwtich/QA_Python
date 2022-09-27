# FUNCTIONS

# def # <- definitions of our functions



"""
def myFunction():
    print('my first functions')

myFunction()

"""


"""
def  userDetails(name, language):
    print('Hello '+ name + ' it is your first ' + language + ' function')

userDetails('Paul', 'Python')

"""

"""
def divide(dividend, divisor):
    if(divisor == 0):
        return False
    else:
        return dividend / divisor

print(divide(5,0))
print(divide(10,2))

"""

# OPTIONAL ARGUMENTS
"""
def new_functions(arg1, arg2 = 'Alfa Romeo'):
    return f'{arg1} {arg2}'

print(new_functions(arg1='car '))
print(new_functions(arg1='car ',arg2='Fiat'))

"""
from functools import partial

def division(x,y):
    return x/y

divide_by_two = partial(division, 2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))




