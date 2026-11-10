
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "This is natural language processing lab"

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

print(filtered_words)
