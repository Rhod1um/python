#!/usr/bin/python3

#Program to get input from user

print("Name: ")
name = input() #input er en funktion. Som med scanner

print("Email: ")
email = input()

print("Mobile number: ")
mobile_number = int(input()) #input er automatisk string, men her vil vi have nummer
#laver man matematik på en streng får man fejl
#her gøres det på én linje,  print og tager input i et:
address = input("Please enter your address: ")
#speciel print, f, gør at den forventer formatted string
print(f"Welcome {name}! You are not registered")

print(type(email))
print(type(mobile_number))

#vigtig at specificere datatypen som skal indtastes så man ikke kan indtaste andet
#den giver fejl valueError
#læs hele erroren
#konvertere nummer til string:
mobile_number = str(mobile_number)
print(type(mobile_number))

