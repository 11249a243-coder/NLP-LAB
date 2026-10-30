from collections import Counter

sentences = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "I", "study", "NLP", "</s>"],
    ["<s>", "You", "love", "NLP", "</s>"]
]

bi = Counter()

for s in sentences:
    for i in range(len(s)-1):
        bi[(s[i], s[i+1])] += 1

frequency = Counter(bi.values())

N1 = frequency[1]
N2 = frequency[2]
N3 = frequency[3]

print("N1:", N1)
print("N2:", N2)
print("N3:", N3)

print("Unseen Probability:", round(N1 / sum(bi.values()), 2))

c1 = 2 * N2 / N1
c2 = 3 * N3 / N2

print("Adjusted Count c*(1):", round(c1, 2))
print("Adjusted Count c*(2):", round(c2, 2))