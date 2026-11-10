
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

words = [
    ("playing", "v"),
    ("studies", "n"),
    ("better", "a"),
    ("cars", "n"),
    ("children", "n")
]

print("Word - Lemmatized Word")

for word, pos in words:
    lemma = lemmatizer.lemmatize(word, pos=pos)
    print(word, "-", lemma)
