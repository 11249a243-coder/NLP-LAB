
from nltk import FreqDist, bigrams
from nltk.tokenize import word_tokenize

tokens = word_tokenize("I like NLP. I like NLP.".lower())

uni = FreqDist(tokens)
bi = FreqDist(bigrams(tokens))
V = len(set(tokens))

mle = bi[("i", "like")] / uni["i"]
add1 = (bi[("i", "like")] + 1) / (uni["i"] + V)

print("MLE:", round(mle, 3))
print("Add-1:", round(add1, 3))