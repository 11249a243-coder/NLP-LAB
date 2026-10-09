from collections import Counter

tokens = "i like nlp i like python".split()
uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
V = len(set(tokens))

pairs = [("i", "like"), ("like", "nlp"),
         ("like", "python"), ("nlp", "i")]
ks = [0.01, 0.1, 0.5, 1.0]

for w1, w2 in pairs:
    print(w1, w2, end=": ")
    for k in ks:
        p = (bi[(w1, w2)] + k) / (uni[w1] + k * V)
        print(round(p, 3), end="  ")
    print()