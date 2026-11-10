
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["the", "boys", "played", "games"]

print("Word Analysis:\n")

for word in words:
    if word == "the":
        print("Word:", word)
        print("Meaning: Definite")
        print("Type: Determiner / Article")

    elif word == "boys":
        print("Word:", word)
        print("Stem:", stemmer.stem(word))
        print("Type: Noun")
        print("Number: Plural")

    elif word == "played":
        print("Word:", word)
        print("Stem:", stemmer.stem(word))
        print("Tense: Past")
        print("Type: Verb")

    elif word == "games":
        print("Word:", word)
        print("Stem:", stemmer.stem(word))
        print("Type: Noun")
        print("Number: Plural")

    print()
