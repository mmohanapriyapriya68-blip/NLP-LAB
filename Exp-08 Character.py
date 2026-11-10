
text = input("Enter the text: ")

letters = 0
digits = 0
special_characters = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special_characters += 1

print("Letters =", letters)
print("Digits =", digits)
print("Special characters =", special_characters)
