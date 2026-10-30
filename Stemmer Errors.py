from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["university", "universe", "alumnus", "alumni"]

for word in words:
    print(word, "->", stemmer.stem(word))