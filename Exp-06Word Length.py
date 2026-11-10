
text = input("Enter the text: ")

words = text.split()

shortest_word = min(words, key=len)
longest_word = max(words, key=len)

total_length = sum(len(word) for word in words)
average_length = total_length / len(words)

print("Shortest word:", shortest_word)
print("Average length:", round(average_length))
print("Longest word:", longest_word)
