
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

words = ["cars", "studies", "playing", "better", "children"]

print("Original Word - Lemmatized Word")

for word in words:
    if word == "better":
        lemma = lemmatizer.lemmatize(word, pos='a')
    elif word == "playing":
        lemma = lemmatizer.lemmatize(word, pos='v')
    else:
        lemma = lemmatizer.lemmatize(word, pos='n')

    print(word, "-", lemma)
