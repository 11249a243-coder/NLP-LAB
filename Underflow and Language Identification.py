from collections import Counter

sentences = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "I", "study", "NLP", "</s>"],
    ["<s>", "You", "love", "NLP", "</s>"]
]

uni = Counter()
bi = Counter()

for s in sentences:
    uni.update(s[:-1])
    for i in range(len(s)-1):
        bi[(s[i], s[i+1])] += 1

V = 8
k = 0.1

def add_k(w1, w2):
    return (bi[(w1, w2)] + k) / (uni[w1] + k * V)

print("P(love|I):", round(add_k("I", "love"), 3))
print("P(study|You):", round(add_k("You", "study"), 3))