
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "NLP is interesting. It is a branch of AI."

sentences = sent_tokenize(text)

print("Original Text:")
print(text)

print("\nSentence Tokens:")
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")
