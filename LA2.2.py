import matplotlib.pyplot as plt
from collections import Counter

tokens = "i like nlp i like python".split()
uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
V = len(set(tokens))

ks = [0.01, 0.1, 0.5, 1.0]

def prob(w1, w2, k):
    return (bi[(w1, w2)] + k) / (uni[w1] + k * V)

seen = [prob("i", "like", k) for k in ks]
unseen = [prob("like", "python", k) for k in ks]

plt.plot(ks, seen, marker="o", label="Seen bigram")
plt.plot(ks, unseen, marker="o", label="Unseen bigram")
plt.xlabel("k")
plt.ylabel("Probability")
plt.legend()
plt.show()