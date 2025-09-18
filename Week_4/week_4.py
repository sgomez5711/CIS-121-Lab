# Steve Gomez

'''
larger_num = int(input("Enter the larger number: "))
smaller_num = int(input("Enter the smaller number: "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num}")
'''


#Question 2

word = input("Enter a word: ")

for i in range(1, len(word) - 1,2):
    result += word[i]

print(f"Output = {result}")

