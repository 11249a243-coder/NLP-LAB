import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>", "<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
bigram_counts = Counter()
trigram_counts = Counter()
vocab = set()
for sent in sentences:
    vocab.update(sent)
    for i in range(len(sent) - 2):
        bigram_counts[(sent[i], sent[i + 1])] += 1
        trigram_counts[(sent[i], sent[i + 1], sent[i + 2])] += 1
V = len(vocab)
def trigram_prob(w1, w2, w3, smoothing=True):
    if smoothing:
        return (trigram_counts[(w1, w2, w3)] + 1) / (
            bigram_counts[(w1, w2)] + V
        )
    denominator = bigram_counts[(w1, w2)]
    if denominator:
        return trigram_counts[(w1, w2, w3)] / denominator
    return 0
print(f"{'Trigram':<30}{'Count':<8}{'P(w3|w1,w2)':<15}")
print("-" * 55)
for (w1, w2, w3), count in trigram_counts.most_common(6):
    probability = trigram_prob(w1, w2, w3)
    print(
        f"({w1}, {w2}, {w3}){'':<6}"
        f"{count:<8}{probability:<15.4f}"
    )
def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 2):
        probability *= trigram_prob(
            tokens[i],
            tokens[i + 1],
            tokens[i + 2]
        )
    return probability
test = "the quick fox"
print(f'\nP("{test}") = {sentence_probability(test):.10f}')