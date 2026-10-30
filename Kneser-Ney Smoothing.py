from collections import defaultdict

sentences = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "I", "study", "NLP", "</s>"],
    ["<s>", "You", "love", "NLP", "</s>"]
]

contexts = defaultdict(set)

for s in sentences:
    for i in range(len(s)-1):
        contexts[s[i+1]].add(s[i])

total = sum(len(v) for v in contexts.values())

for word in ["glasses", "Francisco", "NLP", "love"]:
    count = len(contexts[word])
    probability = count / total
    print(word, ":", round(probability, 3))