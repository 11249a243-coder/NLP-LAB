import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')

words = ["running", "ran", "runs", "runner", "runners"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in words:
    print(word, "Stem:", stemmer.stem(word),
          "Lemma:", lemmatizer.lemmatize(word, pos='v'))