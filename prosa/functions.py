#!/usr/bin/python3

#functions

#bruger def til at definere funktion
#python kan returnere flere variabler

def add(num1, num2, num3=None): #nu kan man enten skrive
#2 eller 3 argumenter. virker ikke hvis der ikke står num3=None
	if num3==None:
		return num1+num2
	else:
		return num1+num2+num3

print(add(4, 5)) #printer kaldet direkte

sum = add(25,25)
print(sum)

print(add(5,6,7)) #virker

num = 3
if num == 5:
	print("1")
	print("2") #ekstra: indentation virker, er del af if

#calculator:

def calculator(num1,num2,kind=None): #sidste parameter har ikke
#en type, kan være  str
	if kind=="+":
		return num1+num2

print("resultat af calculator:", calculator(3,4,"+")) #virker

def maxOfTwo(num1,num2):
	if num1 < num2:
		print(num2, "er størst")
	elif num1 > num2:
		print(num1, "er størst")
	else:
		print("de er ens")


maxOfTwo(7,8)

#flere returværdier:
def  moreReturn(num1, num2):
	return num1, num2

print(moreReturn(1,2))
c, d = moreReturn(1,2) # flere returværdier assignes variabler
print(c,d)

#man acesser lister baglæns ved at skrive minus foran indekstallet

#fortsættelse python II 28. marts

#find længde af list eller string
def find_length(input):
	length=0
	for item in input:
		length +=1
	return length
string = "hello world"
length = find_length(string)
print("length: ", string, "is ", length)

#function find character frequency
def  char_frequency(input):
	freq_dict = {}
	for char in input:
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char]=1
	return freq_dict

input_str="hello world"


