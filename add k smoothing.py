import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z']+", sentence)
tokens = tokenize(corpus)
unigram_counts = Counter(tokens)
bigram_counts = Counter()
for i in range(len(tokens) - 1):
    bigram_counts[(tokens[i], tokens[i + 1])] += 1
V = len(unigram_counts)
def bigram_probability(w1, w2, k):
    numerator = bigram_counts[(w1, w2)] + k
    denominator = unigram_counts[w1] + k * V
    return numerator / denominator
def sentence_probability(sentence, k):
    words = tokenize(sentence)
    probability = 1.0
    for i in range(len(words) - 1):
        probability *= bigram_probability(
            words[i],
            words[i + 1],
            k
        )
    return probability
test_sentence = "the fox runs away"
print("ADD-k SMOOTHING")
print("-" * 40)
print("Test sentence:", test_sentence)
print()
for k in [0.1, 0.5, 1.0]:
    probability = sentence_probability(test_sentence, k)
    print(f"k = {k}")
    print(f"Sentence Probability = {probability:.10f}")
    print()

