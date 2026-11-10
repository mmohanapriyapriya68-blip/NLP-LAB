
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = stopwords.words('english')

print("English Stop Words:")
print(stop_words[:25])
