
from nltk import FreqDist
from nltk.tokenize import word_tokenize

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())
V = len(set(tokens))

print("Vocabulary size:", V)
