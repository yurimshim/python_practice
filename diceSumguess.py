# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:01:50 2018

@author: LG
"""

"""
Roll a pair of dice -> ask the user to guess -> if correct, user gets 1 point
                                                else, computer gets 1 point                       
Repeat 5 times, if user has more points than computer, user wins
else, computer wins
"""
#calculate the sum of dice in advance of asking the user for input
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
diceSum = dice1 + dice2

#roll a pair of dice, and ask the user to guess the sum
#repeat the asking, comparing, and counting process 5 times
times = 0
userTotal = 0
compTotal = 0
while times < 5:
    print("Let's roll a pair of dice!")
    print("*Dice is rolled*")
    guess = int(input("Can you guess the sum of the dice?: "))    
    #if guess equals diceSum, 1 point for the user
    #if not, 1 point for the computer
    if guess == diceSum:
        userTotal += 1
        print("You get a point! You now have %d points" %(userTotal))
    elif guess != diceSum:
        compTotal += 1
        print("You don't get any points. You now have %d points" %(userTotal))
    times += 1
    
#compare the final score and determine who won   
if userTotal > compTotal:
    print("You win by %d points!" %(userTotal - compTotal))
else:
    print("You lose by %d points!" %(compTotal - userTotal))