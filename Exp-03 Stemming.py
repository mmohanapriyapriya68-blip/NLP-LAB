
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "play", "studies", "connected"]

print("Original Word - Stemmed Word")

for word in words:
    print(word + " - " + stemmer.stem(word))
