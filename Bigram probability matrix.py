import re
from collections import Counter, defaultdict

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    return ["<s>"] + re.findall(r"[a-z']+", sentence.lower()) + ["</s>"]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]

bigram_counts = Counter()
unigram_counts = Counter()
vocab = set()

for sentence in sentences:
    vocab.update(sentence)
    unigram_counts.update(sentence[:-1])

    for i in range(len(sentence) - 1):
        bigram_counts[(sentence[i], sentence[i + 1])] += 1

V = len(vocab)

probability_matrix = defaultdict(dict)

for w1 in vocab:
    for w2 in vocab:
        probability_matrix[w1][w2] = (
            bigram_counts[(w1, w2)] + 1
        ) / (unigram_counts[w1] + V)

words = sorted(vocab)

print("Bigram Probability Matrix")
print()

print(f"{'Word':<12}", end="")
for word in words:
    print(f"{word:<10}", end="")
print()

print("-" * (12 + 10 * len(words)))

for w1 in words:
    print(f"{w1:<12}", end="")
    for w2 in words:
        print(f"{probability_matrix[w1][w2]:<10.4f}", end="")
    print()
