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



#Lecture 9/23/25 Week 5 functions and strings

#write code to determine how many letters are in a word

word = 'hello world'

count = 0

for letter in word:
    count += 1
    

print(count)


#To ignore the space:

word = 'hello world'

count = 0

for letter in word:
    if letter != ' ':
        count += 1
    
print(count)



#Write code to determine how many vowels are in a given word
#aeiou

vowels = 'aeiou'

count = 0

word = input('Enter a word: ')

for letter in word:
    if letter in vowels:
        count += 1
        
print(count)



#Write code to determine how many vowels are in a given word. All three outputs at once now.
#aeiou
#word 1 hello world
#word 2 apples and bananas
#word 3 happy times

vowels = 'aeiou'

count = 0

words = ('hello world', 'apples and bananas', 'happy times')

for word in words:
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1    
    print(f'The vowel count in {word} is {count}')



#Write code to determine how many vowels are in a given word. All three outputs at once now.
#aeiou

def vowel_counter(passed_word):
    count = 0
    for letter in passed_word:
        if letter == 'a':
            count += 1
        elif letter == 'e':
            count += 1
        elif letter == 'i':
            count += 1
        elif letter == 'o':
            count += 1
        elif letter == 'u':
            count += 1
        elif letter == 'y':
            count += 1

    print(f'The vowel count in {passed_word} is {count}')

word1 = ('hello word')
word2 = ('apples and bananas')
word3 = ('happy times')

vowel_counter(word1)
vowel_counter(word2)
vowel_counter(word3)


#Lecuture practice 9/25/2025

#Write a function that takes an int adds two, multiplies by 4, printt the result

def my_function(number):
    number += 2
    number *= 4
    return number

def add_ten(number):
    number += 10
    return number


#starting with the value 10, add 2, then multiply it by 4. Take the result and add 2 to it, then multiply by 4 again.

result1 =  add_ten(my_function(10))

result2 = my_function(result1)
print(result2)

#call the function my_function 10 times.


result = 10
for number in range(0, 10):
    result = my_function(result)
print(result)

#call the function my_function 100 times.

result = 10
for number in range(0, 100):
    result = my_function(result)
print(result)


#Write a function that return the product of two arguments.
def product(num1, num2):
    product = num1 * num2
    return product

print(product(4,3))
'''

#In python, a list starts with [ and end with]

x = [] # this is a list with nothing in it.

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

#print the element of the lyst in postion 1

#print(lyst[1])

#print the portion of the list that is 3, False, 4.5

#print(lyst[2:5])

x = 'appl'
print(x)

x += 'e'
print(x)

#lyst.append( element ) will add the element to the end of the lyst.

print(lyst)
lyst.append(12)
print(lyst)