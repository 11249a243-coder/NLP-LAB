
from collections import Counter

tokens = "i like nlp i like nlp i like python i like nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

tests = [
    ("i", "like", "nlp"),
    ("i", "like", "python"),
    ("like", "python", "nlp")
]

alpha = 0.4

def discount(counts, r):
    nr = sum(1 for c in counts.values() if c == r)
    nr1 = sum(1 for c in counts.values() if c == r + 1)
    if nr == 0 or nr1 == 0:
        return r
    return min(r, (r + 1) * nr1 / nr)

for w1, w2, w3 in tests:
    t = tri[(w1, w2, w3)]
    b = bi[(w2, w3)]
    u = uni[w3]

    if t:
        stupid = t / bi[(w1, w2)]
        katz = discount(tri, t) / bi[(w1, w2)]
    elif b:
        stupid = alpha * b / uni[w2]
        katz = alpha * b / uni[w2]
    else:
        stupid = alpha**2 * u / len(tokens)
        katz = alpha**2 * u / len(tokens)

    print((w1, w2, w3))
    print("Stupid Backoff:", round(stupid, 3))
    print("Katz Backoff:", round(katz, 3))