
from collections import Counter

tokens = "i like nlp i like python i like nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

w1, w2, w3 = "i", "like", "nlp"
V = len(set(tokens))

p1 = uni[w3] / len(tokens)
p2 = bi[(w2, w3)] / uni[w2]
p3 = tri[(w1, w2, w3)] / bi[(w1, w2)]

result = 0.1 * p1 + 0.3 * p2 + 0.6 * p3

print("Unigram:", round(p1, 3))
print("Bigram:", round(p2, 3))
print("Trigram:", round(p3, 3))
print("Interpolated probability:", round(result, 3))