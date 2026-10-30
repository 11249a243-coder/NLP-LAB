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

p = 1

test = ["<s>", "You", "study", "NLP", "</s>"]

for i in range(len(test)-1):
    count = bi[(test[i], test[i+1])]
    if count == 0:
        p = 0
        break
    p *= count / uni[test[i]]

print("Sentence Probability:", p)

print("\nWords predicted after love:")
for word in ["NLP", "deep"]:
    print(word, ":", bi[("love", word)] / uni["love"])