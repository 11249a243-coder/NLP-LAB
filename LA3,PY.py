
from nltk import FreqDist, bigrams
from nltk.tokenize import word_tokenize

tokens = word_tokenize("I like NLP. I like Python.".lower())

uni = FreqDist(tokens)
bi = FreqDist(bigrams(tokens))
V = len(set(tokens))

def add1(w1, w2):
    return (bi[(w1, w2)] + 1) / (uni[w1] + V)

print("Seen bigram:", round(add1("i", "like"), 3))
print("Unseen bigram:", round(add1("like", "python"), 3))