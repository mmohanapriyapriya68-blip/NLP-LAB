
text = input("Enter the text: ")

words = text.split()

total_words = len(words)
unique_words = len(set(words))

print("Total words =", total_words)
print("Unique words =", unique_words)
