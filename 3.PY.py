
import nltk
from nltk import bigrams, trigrams, FreqDist
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())

unigram_freq = FreqDist(tokens)
bigram_freq = FreqDist(bigrams(tokens))
trigram_freq = FreqDist(trigrams(tokens))

N = len(tokens)

# Interpolation weights must sum to 1
lambda1, lambda2, lambda3 = 0.1, 0.3, 0.6

def interpolated_prob(w1, w2, w3):
    p_uni = unigram_freq[w3] / N

    p_bi = (
        bigram_freq[(w2, w3)] / unigram_freq[w2]
        if unigram_freq[w2] > 0 else 0
    )

    p_tri = (
        trigram_freq[(w1, w2, w3)] / bigram_freq[(w1, w2)]
        if bigram_freq[(w1, w2)] > 0 else 0
    )

    return (
        lambda1 * p_uni
        + lambda2 * p_bi
        + lambda3 * p_tri
    )

test_triples = [
    ("i", "am", "learning"),
    ("am", "learning", "nlp"),
    ("is", "fun", "to")
]

print(
    f"lambda1={lambda1}, "
    f"lambda2={lambda2}, "
    f"lambda3={lambda3}\n"
)

for w1, w2, w3 in test_triples:
    p = interpolated_prob(w1, w2, w3)
    print(f"P({w3}|{w1}, {w2}) [Interpolation] = {p:.5f}")