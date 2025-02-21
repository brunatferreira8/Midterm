#List example
numbers = [1, 3, 5 , 7, 9]
numbers[1]
numbers[1] = 11 #changes the number in the list
print(numbers) #prints a modified list

#Strings

s = ("Cat")
s[0]
'C'
s[0] = "R"
#An error will appear when I try to change something in the string.
s2 = "R" + s[1:]
#the only thing we can do is create a new string instead of modifying it