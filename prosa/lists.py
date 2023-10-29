#!/usr/bin/python3

#lists

my_list = [1, 'one', 1.0, [2,3,4]]

print(my_list) #viser liste på række

for items in my_list: #viser liste nedad
	print(items)

#få værdi fra indexnummer:
print(my_list[2])
#værdi i liste inde i liste:
print(my_list[3][2]) #printer 4

#in-built list funktioner:

print("lægde: ", len(my_list))
print(my_list.append('four')) #append for at lægge nyt i listen
#^ printer none da det ikke giver mening at printe at man lægger
#noget i listen...
print(my_list)

#concatenation:
print([1,2,3]+[4,5,6])
#repitition:
print([1]*4)
#membership:
print(3 in [1,2,3]) #søger efter 3, giver true

#slicing:
print(my_list[::2]) # tæller både forfra og bagfra, skipper 
#hver anden position og printer det
#reverse the list:
print(my_list[::-1])

#count value in list:
print(my_list.count(1))

#dictionary er en datatype som object i python, key:value pair
dict = {"Gino":5, "Nora":10}

print(dict['Gino']) #giver value for navnet/key'en
#i stedet for index position om med lister skriver man key

my_dictionary = {
	"name":"moon",
	"class":"BEIT",
	"kommune":"ballerup"
}
print(my_dictionary)
print(my_dictionary["kommune"])

for key,value in my_dictionary.items():
	print(key,":", value)
#skal have .items() ellers får man fejl

for value in my_dictionary.values():  #printer kun values
	print(value)

my_dictionary["workplace"]="prosa" #appender
print(my_dictionary)
