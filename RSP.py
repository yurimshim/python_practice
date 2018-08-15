# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:51:12 2018

@author: LG
"""
#create dictionary of possible keys and embedded dictionary of other keys and outcomes
import random 
RSP = {"rock": {"rock": "ditto", "scissors": "win", "paper": "lose"}, 
       "scissors": {"rock": "lose", "scissors": "ditto", "paper": "win"},
       "paper": {"rock": "win", "scissors": "lose", "paper": "ditto"}}
user_point = 0
comp_point = 0
match = 0
while match < 3:
    #prompt the user for input
    user_rsp = input("Rock, Paper, Scissors!:")
    comp_rsp = random.choice(list(RSP.keys()))
    #get the possible outcome from the dictionary
    outcome_temp = RSP[user_rsp][comp_rsp]
    #compare the points
    if outcome_temp == "win":
        print("You won!")
        user_point += 1
    elif outcome_temp == "lose":
        print("You lost!")
        comp_point += 1
    else:
        continue
    match += 1
#after all 3 matches, determine a winner
if user_point > comp_point:
    print("The user wins the computer by %d points!" %(user_point - comp_point))
else:
    print("The computer wins the user by %d points!" %(comp_point - user_point))