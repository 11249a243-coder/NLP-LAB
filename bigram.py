import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()
for sent in sentences:
    unigram_counts.update(sent[:-1])
    vocab.update(sent)
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1
V = len(vocab)
def bigram_prob(w1, w2, smoothing=True):
    if smoothing:
        return (bigram_counts[(w1, w2)] + 1) / (unigram_counts[w1] + V)
    else:
        if unigram_counts[w1]:
            return bigram_counts[(w1, w2)] / unigram_counts[w1]
        return 0
print(f"{'Bigram':<25}{'Count':<8}{'P(w2|w1) smoothed':<20}")
print("-" * 55)
for (w1, w2), count in bigram_counts.most_common(8):
    probability = bigram_prob(w1, w2)
    print(f"({w1}, {w2}){'':<10}{count:<8}{probability:<20.4f}")
def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 1):
        probability *= bigram_prob(tokens[i], tokens[i + 1])
    return probability
test = "the fox runs"
print(f'\nP("{test}") = {sentence_probability(test):.10f}')