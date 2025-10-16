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



#Lecture practice 9/30/25

lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(x[2])
#print(x[1:4])

#for element in lyst:
 #   print(element)

#print(lyst)
#lyst.append('Saturday')
#lyst.append('Sunday')
#print(lyst)


#print nes in Wednesday only

#print(lyst[2][3:6])

#x = 'Wednesday'
#print(x[3:6])


#print(lyst)

#lyst[4]= 'Funday'

#print(lyst)

x = 'apple'
y = x
print(x)
print(y)

x += 's'
print(x)
print(y)

#immuatble object


#mutable object

#workdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
#y = x

#print(x)
#print(y)

#print(workdays)
#workdays[4] = 'Funday'
#print(workdays)

#print(x)
#print(y)


# Write a function that takes a string as an agrument, and returns a list containing all of the words in that string.

my_word = "Peter Piper picked a peck of pickled peppers."
result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']
          

def string_to_list(word):
    words = []
    # collect a word
    built_word = ''
    for letter in word:
        if letter == ' ':
            # add built_word into the list
            words.append(built_word)
            built_word = ''
        #once we have a full word, let's add it to the list of words.
        else:
            built_word += letter
        words.append(built_word)
        built_word = ''
            


    #once we have a full word, let's add it to the list of words.
    return words



print(string_to_list(word))

def string_to_list(word):
    words = []
    built_word = ''
    for index in range(len(word)) :
        if word[index] == ' ' or index == len(word)-1:
            words.append(built_word)
            built_word = ''
        else:
            built_word += word[index]
    return words


print(string_to_list(my_word))




#Lecture practice 10/2/2025


def string_to_list(word):
    words = []
    # collect a word
    built_word = ''
    vowel_count = 0
    for letter in word:
       # print(letter, vowel_count)
        if letter == ' ':
            # add built_word into the list if amount of vowels >= 2.
            if vowel_count >= 2:
                words.append(built_word)
            built_word = ''
            vowel_count = 0
        #once we have a full word, let's add it to the list of words.
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count += 1

    if vowel_count >= 2:
     words.append(built_word)
    return words


    

#my_word = "Peter Piper picked a peck of pickled peppers."
#result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']


# write a function that takes a string as an argument, and returns a list containing all of the words in that string.


phonebook = {'matt':5073891438, 'ashley': 12345}
#print(phonebook)

#to add to. a dictionary, we use name_of_dict [ key ] = value
phonebook['waters'] = 789
print(phonebook)

# to look up a value in a dictionary, we use name_of_dict[ key ]
print(phonebook['matt'])
#print(phonebook['martensen'])

for person in phonebook.keys():
    print(person, phonebook[person])


# write a function that takes a string as an argument and returns a dictionary contaonong all pf the unique words in that string.

    def string_to_dictionary(word):
        string_as_list = word.split()
        word_dictionary = {}
        for word in string_as_list:
            word_dictionary[word] = 'in word'
        return word_dictionary
    
print(string_to_dictionary)(my_words)



# Lecture practice 10/7/2025

my_word = "peter piper picked a peck of pickled peppers."

# Write a function that returns a dictionary containing how many times each letter appears.


def letter_counter(word):
    letter_dictionary = { }
    for letter in word:
        if letter in letter_dictionary:
            #add in key value pair. What are key and value?
            letter_dictionary[letter] = letter_dictionary[letter] + 1
            #letter_dictionary[letter] += 1
        else: # key is NOT in dictionary.
            # add in key value pair. What are key and value?
            letter_dictionary[letter] = 1

    return letter_dictionary

my_word = "peter piper picked a peck of pickled peppers."
letter_dict = letter_counter(my_word)

for letter in letter_dict:
    print(letter, letter_dict[letter])

# Result should look similat to something like this: d = {'p':9,'e':???}



def add_three(x):
    y = x + 3
    return y

var0 = 7
var1 = add_three(var0)

print(y)



# Lecture practice 10/9/25


'''

# Lecture practice 10/14/25
# Debugging

def string_to_list_with_vowels(word):
    words = []
    #collect a word
    built_word = ''
    vowel_count = 0
    for letter in word:
        if letter == ' ':
            words.append(built_word)
        else:
            built_word = ''
            built_word += letter
    return words

my_word = 'peter piper picked a peck of pickled pepprs'
print(string_to_list_with_vowels(my_word))

# Lecture 10/16/25

