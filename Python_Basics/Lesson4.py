# Conditional Statements

firstName = 'Pierre'
lastName = 'Swtich'
userAge = 30

if lastName == 'Swtich' and userAge == 30:
    print('Hello Swtich, you are 30 yo')
else:
    print('It is not you!')


print('')

# Other option -> "in" which allow us to give on of matching phrases/values

if firstName in ['Pierre','Adam','John'] and userAge == 30:
    print('Cześć '+ firstName + ', you have: ' + str(userAge) + ' yo!')
else:
    print('It is not you!')


# Other example

print('')

variable0 = -1
variable1 = 1
variable2 = 2
variable3 = 3

if variable1 > 0:
    print('1')
elif variable2 < 0:
    print('2')
else:
    print('3')

#Other example

if variable0 > 0:
    print('1')
elif variable2 < 0:
    print('2')
else:
    print('Only False, no H approved')