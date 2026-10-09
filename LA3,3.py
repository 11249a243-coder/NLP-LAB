
from collections import Counter

tokens = "i like nlp i like python i like nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

p1 = uni["nlp"] / len(tokens)
p2 = bi[("like", "nlp")] / uni["like"]
p3 = tri[("i", "like", "nlp")] / bi[("i", "like")]

l1, l2, l3 = 0.1, 0.3, 0.6
result = l1*p1 + l2*p2 + l3*p3

print("Unigram MLE:", round(p1, 3))
print("Bigram MLE:", round(p2, 3))
print("Trigram MLE:", round(p3, 3))
print("Final probability:", round(result, 3))