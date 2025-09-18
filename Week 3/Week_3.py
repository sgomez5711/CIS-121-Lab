# Created by Steve Gomez On Sept 11 2025
'''
number = input("Enter a number: ")

if number > 0:
    print("Its Postive")
elif number > 1000: 
    print("Its largely Postive")
elif number > 100000:
    print("Its a very large number")
else: 
    print("Its is a negative number")
'''

standards = input("Enter your standard: ")

if standards >= 53:
    print("A")
elif standards >= 51 and standards < 53:
    print("A-")
elif standards >= 49:
    print("B+")
elif standards >= 47:
    print("B")
elif standards >= 45:
    print("B-")
elif standards >= 43:
    print("C+")
elif standards >= 40:
    print("C")
