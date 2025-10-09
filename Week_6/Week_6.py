'''
# Question 5:

def hailstone_seq(number):
    # Create an empty list
    output_list = []
    # Code it here !
    while number >= 1:
        # While loop till 1
        if number % 2 == 0:
            # Is even
            number /= 2
            #number = number / 2
        else:
            # Is Odd
            number = (3 * number) + 1
        print(number)
        # Add the result to the output list.
        output_list.append(number)

    return output_list

print(f"{hailstone_seq}(25)")




# Question 9 

# Function takes in a list of cards
def count(list_of_cards):
    
    for card in list_of_cards:
     
     temp_card = str(card)

     if temp_card in ['2', '3', '4', '5', '6']:
         points += 1
         #
     elif temp_card in ['10', 'j', 'q', 'k']:
         points += -1

    return points

# Create the list of cards
cards = [5, 9, 10, 3, "j", "a", 4, 8, 5]

print(f"Total Count : {count(cards)}")



# Try converting everything into a string
items = ['1', '2', '3', 'a', 'b']

for item in items:
     if str(item) in ['1', '2', '3', 'a', 'b']:
        print("True")
    else:
        print("False")



# Question 19
# How can I iterate through each word, and extract the first letter
# for word in words:
# first_letter = word[0]

# Combine the extracted letters and compare with string s
# s += first_letter


# is length of s is different from the length of words , false
# len(s) == len(words):

def is_acronym(s, words):
    # if len is s != words - > false
    current_word = wprds[i]


    if len(s) != len(words):
        return False
    
    # iterate through each words
    for wi in range (0, len(words)):
        if words[i] == "":
            return False
        if s[i] != words[i][0]:


    #   if word == "" -> false


    #   if word[0] == s[i]

    return True

s = "abc"
words = ["alice", "bob", "charlie"]

print(f"{is_acronym(s, words)}")


'''

def hamming_distance(str1,str2):
    total = 0
    for letters in word:
        if str1 > word[i]:
            total += 1
        elif str2 > word[i]:
            total += 1
        else:
            total == 0
    return hamming_distance