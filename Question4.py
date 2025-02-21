def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

#list of strings
numbers = {
    "A": "6800923757255865070000705685527573290086",
    "B": "1414884937242655719669145562427394884141",
    "C": "9847255590886266818998186626880955527489",
    "D": "6892149109325320763773670235239019412986"
}

#check through the numbers
for key, num in numbers.items():
    if not palindrome(num):
        print(f"Option {key}) {num} is NOT a palindrome.")
    else:
        print(f"Option {key}) {num} is a palindrome.")
