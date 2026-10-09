
import nltk
from nltk import bigrams, FreqDist
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())

unigram_freq = FreqDist(tokens)
bigram_freq = FreqDist(bigrams(tokens))
vocab_size = len(unigram_freq)

def addk_prob(w1, w2, k):
    numerator = bigram_freq[(w1, w2)] + k
    denominator = unigram_freq[w1] + (k * vocab_size)
    return numerator / denominator

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

k_values = [0.01, 0.1, 0.5, 1.0]

print(f"{'Bigram':<25}", end="")
for k in k_values:
    print(f"{'k=' + str(k):<12}", end="")
print()

for w1, w2 in test_pairs:
    print(f"({w1}, {w2}){' ' * (25 - len(w1) - len(w2) - 4)}", end="")

    for k in k_values:
        p = addk_prob(w1, w2, k)
        print(f"{p:<12.5f}", end="")

    print()