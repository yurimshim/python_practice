# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:07:31 2018

@author: LG
"""
"""
Vending machine has drinkStock(dict of number of drinks available),
drinkPrice(dict of rice of drinks),cashUnit(list of available unit of cash for paying),
and revenue(cash earned)
asks user for type, number of drinks he/she wants and checks if available
if drinkStock[desired drink] >= num of desired drink, sell. else, no go.
then ask user for cash. if cash matches exactly the price, give product. else, no.
then return the change.
Then update the drinkStock and revenue
"""
def VendingMachine(customerName):
    #welcoming message by the polite little machine
    print("Hello,", customerName, "! Came to buy a drink?")
    
    #initial status
    drinkStock = {"Coke": 10, "Sprite": 12, "Dr. Pepper": 8, "Lemonade": 5, "Chocolate milk": 4}
    drinkPrice = {"Coke": 2200, "Sprite": 2500, "Dr. Pepper": 3300, "Lemonade": 3500, "Chocolate milk": 5100}
    cashUnit = [100, 500, 1000]
    revenue = 0
    
    #user comes, flash the type and price
    print("Drinks available:", drinkStock) 
    print("Price:", drinkPrice)
    print("Pay by cash:", cashUnit)
    
    #prompt the user for desired drink and return the drink and price
    wantedDrink = input("What is your desired drink?")
    wantedNum = int(input("How many do you want?"))
    
    #check if vending machine has the wanted number of the wanted drink
    if wantedDrink in drinkStock.keys() and wantedNum <= drinkStock[wantedDrink]:
        print(customerName, ", Drink of desired number is available!")
    else:
        print(customerName, ", Drink of desired number not available!")
    
    #prompt the user to pay, then compare
    shouldPay = wantedNum * int(drinkPrice[wantedDrink])
    totalPay = 0
    while totalPay < shouldPay:
        print("You have paid:", totalPay)
        pay = int(input("Please pay by 100, 500, or 1000:"))
        if pay not in cashUnit:
            pay = int(input("Please pay by 100, 500, or 1000:"))
        else:
            totalPay += pay
    #give change and drink        
    change = totalPay - shouldPay
    print("Here is your %d %s" %(wantedNum, wantedDrink))
    print("And here is your change:", change)
    print("Have a nice day,", customerName)
    #subtract the number of drinks from the stock
    drinkStock[wantedDrink] -= wantedNum
    revenue += shouldPay
    print("Money earned:", revenue)    