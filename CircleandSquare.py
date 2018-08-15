# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:48:32 2018

@author: LG
"""

"""
This program asks a user for a shape,
calculates its area,
and prints it out for the user
"""
#Ask the user for a shape
print("The calculator is starting up!")
option = input("Enter C for circle or T for Triangle ")

#ask the user again if their input is not valid
if option != "C" and option != "T":
    option = print("Please type in a valid input ")

#calculate the area of a circle if the user chooses a circle
elif option == "C":
    radius = float(input("Please put in the radius "))
    area = 3.14159 * (radius ** 2)
    print(area)
    
#calculate the area of a triangle if the user chooses a triangle
else:
    height = float(input("Type the height:"))
    side = float(input("Type the side:"))
    area = (1/2) * height * side
    print(area)
    
  