# Steve Gomez

'''
larger_num = int(input("Enter the larger number: "))
smaller_num = int(input("Enter the smaller number: "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num}")



#Question 2

word = input("Enter a word: ")
result = ""
# First start point, Ending Point, step size
for i in range(1, len(word) - 1,2):
    result += word[i]

print(f"Output = {result}")


#Question 3

#print all of the even number betwen 37-1050 (inclusively)

for number in range (38,1051,2):
    print(number)

# OR bottom code

for number in range(37,1051):
    if number % 2 == 0:
        print(number)
'''


#Question 4
word = ""

#While loop that runs forever
while True:
    # Read the user input
    user_in = input("Enter a letter: ")
    # if the user tyoed "done" we stop !
    if user_in == "done":
        break
    else:
        # Else lets add letter into the word
        word += user_in

# Print out the final word
print(f"The final word is {word}")
