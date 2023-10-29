#!/usr/bin/python3

#for loop
my_string = "hello world"

for alphabet in my_string:
	print(alphabet)


print("i am out of for-loop")

my_list = ["apples", "oranges", "kiwis", "almonds"]
for element in my_list:
	print(element)
	print("i loop?") #her er den stadig i loop modsat med if

print("out of second for-loop")

#while loop
print("while:")
counter = 0

while counter <= 5:
	print(counter)
	counter += 1

print("out of while")

