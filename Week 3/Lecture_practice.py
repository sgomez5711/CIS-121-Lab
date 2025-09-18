# Week 4 Loops

#print the numbers 1-10
#number = 1

#while True <= 10:
 #   print(number)
  #  number += 1


#print the even numbers between 1-10
'''
number = 2
while number <= 10:
    print(number)
    number += 2


number = 1
while number <= 10:
    if number % 2 == 0: #is even:
        print(number)
    number += 1

number = int(input("Enter a number: "))
while number <= 10:
    if number % 2 == 1: #is even:
        number += 1
    print(number)
    number += 2



#print all odd number between 5 and some
#number given by the user.

start_number: 5
end_number = int(input('Enter a number: '))

while start_number <= end_number:
    if start_number % 2 == 1:
        print(start_number)
    start_number += 1

#print all even numbers that are not divisible by 3
number = 0

while number < 50:
    number += 1
    if number % 2 == 0:
        if number % 3 == 0:
            #do nothing
            # and skip the rest of the code
            continue
        print(number)


#write a program that adds numbers until
#the user says stop

total = 0

user_number = input('Enter a number or type q to end: ')

while user_number != 'q':
    total += int(user_number)
    user_number = input("enter a number ot type q to end: ")

print(f'total = {total}')


#print all of the even number betwen 1-10
for number in range (2,11,2):
    print(number)

for number in range(1,11):
    if number % 2 == 0:
        print(number)


#print all of the odd number between 5 and some
#user given value (inclusivly)

user_number = int(input("enter a number: "))
for number in range (5, user_number + 1):
    if number % 2 == 1:
        print(number)

      
#find the sum of the user entered values until the
#user types q (for done)

total = 0
user_input = input("enter a number or type q to exit: ")

while user_input != 'q':
    total += int(user_input)
    user_input = input("enter a number or type q to exit: ")


from random import randint
value = randint(0, 1)   # 0 or 1

guess = input("Guess heads or tails: ")   # expect exactly "heads" or "tails"

if value == 0:
    result = "heads"
else:
    result = "tails"

if guess == result:
    print("Correct!")
else:
    print("Incorrect. It was", result)
'''

x = int(input("Enter a number: "))
y = int(input("Enter a another number: "))
z = int(input("Enter a another number: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z , y

print(x,y,z)