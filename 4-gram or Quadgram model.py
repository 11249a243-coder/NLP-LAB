import re
from collections import Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    return ["<s>", "<s>", "<s>"] + re.findall(
        r"[a-z']+", sentence.lower()
    ) + ["</s>"]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]

trigram_counts = Counter()
quadgram_counts = Counter()
vocab = set()

for sentence in sentences:
    vocab.update(sentence)

    for i in range(len(sentence) - 3):
        trigram_counts[
            (sentence[i], sentence[i + 1], sentence[i + 2])
        ] += 1

        quadgram_counts[
            (
                sentence[i],
                sentence[i + 1],
                sentence[i + 2],
                sentence[i + 3]
            )
        ] += 1

V = len(vocab)

def quadgram_probability(w1, w2, w3, w4):
    numerator = quadgram_counts[(w1, w2, w3, w4)] + 1
    denominator = trigram_counts[(w1, w2, w3)] + V
    return numerator / denominator

print(f"{'Quadgram':<45}{'Count':<8}{'Probability':<12}")
print("-" * 65)

for quadgram, count in quadgram_counts.most_common(10):
    probability = quadgram_probability(*quadgram)
    print(f"{str(quadgram):<45}{count:<8}{probability:<12.4f}")

def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1.0

    for i in range(len(tokens) - 3):
        probability *= quadgram_probability(
            tokens[i],
            tokens[i + 1],
            tokens[i + 2],
            tokens[i + 3]
        )

    return probability

test = "the quick brown fox"
print(f'\nP("{test}") = {sentence_probability(test):.10f}')