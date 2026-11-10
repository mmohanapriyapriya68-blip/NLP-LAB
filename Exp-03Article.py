
word = input("Enter a word: ")

if word[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"

print(article, word)
