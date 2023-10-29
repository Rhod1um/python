#!/usr/bin/python3
#String examples

String1 = "python module 1"
print("this string saved with double qoutes")
print(String1)

String2 = 'strings session'
print("string saved with single qoutes")
print(String2)

#slice string, få session, s er på 8' plads
#enten skal siste tal efter : være hvor strengen slutter eller
#den kan være tom så den automatisk stopper ved enden af strengen

print(String2[8:])
print(String2[:7]) #får første ord
#samme gøres ved at slice lists

#at få index position kan læses både forfra og bagfra
#concat for at sammensætte strings:
substring1 = "hello"
substring2 = "world"
newString = substring1 + " " + substring2

print(newString)

#length af string
print(len(newString))

print("hello" in newString) #in søger, her søges om hello er
#i newString, giver true

#conditional statements - if else

