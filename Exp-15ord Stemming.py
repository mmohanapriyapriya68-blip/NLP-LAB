
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["unhappy", "playing", "played", "happiness", "connected"]

print("Word - Stem")

for word in words:
    stem = stemmer.stem(word)
    print(word, "-", stem)
