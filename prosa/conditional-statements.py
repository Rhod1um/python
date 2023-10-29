#!/usr/bin/python3
#if else statements

#number = int(input("enter number 1-10: "))
number = 10

if number == 10:
	print(number)
	print("stadig i if?") #indentation bestemmer om man
#stadig er i if

if number == 10:
	print(number)
else:
	print(number, "is not 10")

print("if else block is done")
#multiple line comment:
"""
 jk
fen
"""

#example of if else:

name = input("enter your name: ")
age = int(input("enter your age: "))
card = input("do you have a card? ")
card = card.lower() #gør det til lower case

if age < 18:
	print("not allowed")
elif age >= 18 and card == "yes":    #elif for else if
	print("welcome")
else:
	print("you need to register")

#to typer loops: for og while 

