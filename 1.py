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

def add1_prob(w1, w2):
    numerator = bigram_freq[(w1, w2)] + 1
    denominator = unigram_freq[w1] + vocab_size
    return numerator / denominator

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

print(f"Vocabulary size (V) = {vocab_size}\n")
print(f"{'Bigram':<25}{'Count':<8}{'P(w2|w1) Add-1':<15}")

for w1, w2 in test_pairs:
    p = add1_prob(w1, w2)
    bigram = f"({w1}, {w2})"
    print(f"{bigram:<25}{bigram_freq[(w1, w2)]:<8}{p:.5f}")

