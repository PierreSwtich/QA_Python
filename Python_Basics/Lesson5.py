# FOR & WHILE LOOP

numbers = [1,2,3,4,5]

# Tis loop will go up to 5 times an print each time the number of the i++

for i in numbers:
    print(i)

# This loop will go up to 5 times and for each loop it prints all the list data 

for i in numbers:
    print(numbers)

print('')

# range() is a python function which return numbers in a range

for i in range(10):
    print(i)

print('')

print('range step')

print('')

for i in range(15,18):
    print(i)

print('')

# other loops

meter = 0

# The loop will continue until the var number will be smaller than 10

#while meter < 10:
 #   print(meter)
  #  meter += 1

# Break & Continue
print('')

print('Break')

print('')


# while True:
#     print(meter)
#     meter += 1
#     if meter >= 5:
#         break

for x in range(20):
    if x % 2 == 0:
        continue
    print(x)