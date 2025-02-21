import random

#Create an empty list
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

#Modify the list
for i in range(len(random_numbers)):  #Select random numbers from the list
    if random_numbers[i] > 50:  # Check if number is greater than 50
        random_numbers[i] = random.randint(20, 30)  #if the number is greater replace it with a random number between 20 and 30
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"  #if number is less, replace it with XX

#Print new list
print(random_numbers)
