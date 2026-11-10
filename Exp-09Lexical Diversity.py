
text = input("Enter the text: ")

words = text.split()

total_words = len(words)
unique_words = len(set(words))

lexical_diversity = unique_words / total_words

print("Lexical Diversity =", round(lexical_diversity, 2))
