
from collections import Counter

tokens = "i like nlp i like python i enjoy nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))

w2, w3 = "i", "enjoy"

p = bi[(w2, w3)] / uni[w2]

for alpha in [0.4, 0.7]:
    print("Alpha:", alpha)
    print("Probability:", round(alpha * p, 3))