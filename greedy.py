'''
This code will calculate how many coins will be used for change based on
the amount owed. Also, it will reprompt the user if the user inputs a negative
value.

By Ben
'''

#For reprompt
change = float(input("How much change is owed? "))

while change < 0:
    change = float(input("How much change is owed? "))

change = change * 100

#Calculations

remainder = change % 25
coins = (change - remainder)/25

change = remainder

remainder = change % 10
coins = coins + (change - remainder)/10

change = remainder

remainder = change % 5
coins = coins + (change - remainder)/5

change = remainder

remainder = change % 1
coins = coins + (change - remainder)/1

change = remainder

print("You need", int(coins), "coins")
