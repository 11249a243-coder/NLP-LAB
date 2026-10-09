from collections import Counter
import math

train = "i like nlp i like python".split()
test = "i like nlp".split()

uni = Counter(train)
bi = Counter(zip(train[:-1], train[1:]))
V = len(set(train))

for k in [0.01, 0.1, 0.5, 1.0]:
    log_sum = 0

    for w1, w2 in zip(test[:-1], test[1:]):
        p = (bi[(w1, w2)] + k) / (uni[w1] + k * V)
        log_sum += math.log(p)

    perplexity = math.exp(-log_sum / (len(test) - 1))
    print("k =", k, "Perplexity =", round(perplexity, 3))