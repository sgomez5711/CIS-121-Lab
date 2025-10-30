# Question 4

def find_winner(player1 = "rock", player2 = "rock"):
    
    if player1 == player2:
        return "It is a Tie"
    
    if (player1 == "rock" and player2 == "scissors"):
        return "Player 1 Wins"
    elif (player1 = "scissors" and player2 =="paper"):
         return "Player 1 Wins"
    elif (player1 == "paper" and player2 == "rock"):
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

# Question 8

def decending_order(num1, num2 = 15, num3 = 3):

    a, b, c = num1, num2, num3


# a = num1
# b = num2
# c = num3

    if a < b:
        a, b = b, a

    if a < c:
        a, c = c, a

    if b < c:
        b, c = c, b

    return [a ,b, c]

# Question 15

def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    
'''
# Shorter way of writing the same thing!
#def is_negative(num):
#    return num < 0

'''

def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        False

'''

#Short way of writing the same thing again
def is_oddd(num):
    return num % 2 != 0 

'''


def report_negative_odds(lyst):
    output = []


# We need to check each number , if it is negative and odd.
    for num in lyst:
        if is_negative(num) and is_odd(num):
        output.append(num)


    return output 