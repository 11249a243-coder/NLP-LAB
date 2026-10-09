
from collections import Counter

tokens = "i like nlp i like python i like nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

p1 = uni["nlp"] / len(tokens)
p2 = bi[("like", "nlp")] / uni["like"]
p3 = tri[("i", "like", "nlp")] / bi[("i", "like")]

best = 0
best_weights = (0, 0, 1)

for a in range(11):
    for b in range(11 - a):
        c = 10 - a - b

        l1 = a / 10
        l2 = b / 10
        l3 = c / 10

        p = l1*p1 + l2*p2 + l3*p3

        if p > best:
            best = p
            best_weights = (l1, l2, l3)

print("Best weights:", best_weights)
print("Highest probability:", round(best, 3))