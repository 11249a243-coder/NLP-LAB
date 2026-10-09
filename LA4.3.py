
from collections import Counter

tokens = "i like nlp i like python i enjoy nlp".split()

uni = Counter(tokens)
bi = Counter(zip(tokens[:-1], tokens[1:]))
tri = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

tests = [
    ("i", "like", "nlp"),
    ("i", "like", "python"),
    ("like", "i", "enjoy"),
    ("like", "python", "enjoy")
]

counts = {"Trigram": 0, "Bigram": 0, "Unigram": 0}

for w1, w2, w3 in tests:
    if tri[(w1, w2, w3)] > 0:
        counts["Trigram"] += 1
    elif bi[(w2, w3)] > 0:
        counts["Bigram"] += 1
    else:
        counts["Unigram"] += 1

for level in counts:
    percent = counts[level] / len(tests) * 100
    print(level, ":", round(percent, 1), "%")