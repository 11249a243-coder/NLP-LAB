
from collections import Counter

tokens = "i like nlp i like python i like nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

p1 = uni["nlp"] / len(tokens)
p2 = bi[("like", "nlp")] / uni["like"]
p3 = tri[("i", "like", "nlp")] / bi[("i", "like")]

result = 0.6 * p1 + 0.3 * p2 + 0.1 * p3

print("Interpolated probability:", round(result, 3))