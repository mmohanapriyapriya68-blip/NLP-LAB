
from collections import Counter

text = input("Enter the text: ")

words = text.split()

word_frequency = Counter(words)

print("Word Frequencies:")

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
