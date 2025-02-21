def find_pattern(text):
    count = 0  #initial count

    words = text.split()  # will split the text

    for word in words:
        if len(word) > 2 and word[:2] == "un" and word[-2:] == "an":  # checks conditions
            count += 1  # Increment counter if condition is met

    return count  # Return total matches


# Example:
text = "unbroken unhuman unusual uncertain uncan undo unnan"
result = find_pattern(text)
print("Number of matches:", result)
