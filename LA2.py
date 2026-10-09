from nltk import FreqDist, bigrams
from nltk.tokenize import word_tokenize

corpus = "I like NLP. I like Python."
tokens = word_tokenize(corpus.lower())

uni = FreqDist(tokens)
bi = FreqDist(bigrams(tokens))
V = len(set(tokens))

def add1(w1, w2):
    return (bi[(w1, w2)] + 1) / (uni[w1] + V)

print("P(like|i):", round(add1("i", "like"), 3))
print("P(python|like):", round(add1("like", "python"), 3))