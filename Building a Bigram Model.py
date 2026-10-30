from collections import Counter

sentences = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "I", "study", "NLP", "</s>"],
    ["<s>", "You", "love", "NLP", "</s>"]
]

unigrams = Counter()
bigrams = Counter()

for sentence in sentences:
    unigrams.update(sentence[:-1])
    for i in range(len(sentence) - 1):
        bigrams[(sentence[i], sentence[i + 1])] += 1

def probability(w1, w2):
    return bigrams[(w1, w2)] / unigrams[w1]

print("Unigram Counts:")
for word in ["<s>", "I", "love", "NLP"]:
    print(word, unigrams[word])

print("\nBigram Counts:")
for pair in [("I", "love"), ("I", "study"),
             ("love", "NLP"), ("love", "deep")]:
    print(pair, bigrams[pair])

print("\nProbabilities:")
print("P(I|<s>):", probability("<s>", "I"))
print("P(love|I):", probability("I", "love"))
print("P(NLP|love):", probability("love", "NLP"))
print("P(</s>|NLP):", probability("NLP", "</s>"))