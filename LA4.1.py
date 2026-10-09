
from collections import Counter

tokens = "i like nlp i like python i enjoy nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

tests = [
    ("i", "like", "nlp"),
    ("i", "like", "python"),
    ("i", "enjoy", "nlp"),
    ("like", "python", "i")
]

alpha = 0.4

for w1, w2, w3 in tests:
    if tri[(w1, w2, w3)] > 0:
        p = tri[(w1, w2, w3)] / bi[(w1, w2)]
        level = "Trigram"
    elif bi[(w2, w3)] > 0:
        p = alpha * bi[(w2, w3)] / uni[w2]
        level = "Bigram"
    else:
        p = alpha * alpha * uni[w3] / len(tokens)
        level = "Unigram"

    print((w1, w2, w3), level, round(p, 3))