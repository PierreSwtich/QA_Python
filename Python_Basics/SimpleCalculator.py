def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print('')
print("Pick an operation by providing a correct value.")
print('')
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print('')

while True:
    choice = input("Choose an operation (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if choice == '1':
            print('')
            print(int(add(num1, num2)))
            print('')
        if choice == '2':
            print('')
            print(int(subtract(num1, num2)))
            print('')
        if choice == '3':
            print('')
            print(int(multiply(num1, num2)))
            print('')
        if choice == '4' and num2 != 0:
            print('') 
            print("{:.2f}".format(divide(num1, num2))) # No int() function as the divide can have a declimal point, alos i have used the .format option to limit the declimal point to 2
            print('') 
        if choice == '4' and num2 == 0:
            print('') 
            print('You cannot divide by 0')
            print('')
    else:
        print('')
        print("You can only choose from 1-4 as the calculator do not have any other functionalites so far.")
        print('')