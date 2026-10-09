
from nltk import FreqDist, bigrams, trigrams
from nltk.tokenize import word_tokenize

tokens = word_tokenize("I like NLP. I like Python.".lower())

bi = FreqDist(bigrams(tokens))
tri = FreqDist(trigrams(tokens))
V = len(set(tokens))

def trigram_prob(w1, w2, w3):
    return (tri[(w1, w2, w3)] + 1) / (bi[(w1, w2)] + V)

print("P(NLP|i like):", round(trigram_prob("i", "like", "nlp"), 3))