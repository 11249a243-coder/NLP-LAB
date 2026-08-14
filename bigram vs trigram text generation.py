import re
import random
from collections import defaultdict, Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z']+", sentence)
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
# BIGRAM MODEL
bigram_model = defaultdict(Counter)
for sent in sentences:
    for i in range(len(sent) - 1):
        bigram_model[sent[i]][sent[i + 1]] += 1
# TRIGRAM MODEL
trigram_model = defaultdict(Counter)
for sent in sentences:
    for i in range(len(sent) - 2):
        key = (sent[i], sent[i + 1])
        trigram_model[key][sent[i + 2]] += 1
def generate_bigram(max_len=10):
    word = "the"
    result = [word]
    for _ in range(max_len - 1):
        next_words = bigram_model[word]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        word = random.choices(words, weights=counts, k=1)[0]
        result.append(word)
    return " ".join(result)
def generate_trigram(max_len=10):
    w1 = "the"
    w2 = "quick"
    result = [w1, w2]
    for _ in range(max_len - 2):
        next_words = trigram_model[(w1, w2)]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        w3 = random.choices(words, weights=counts, k=1)[0]
        result.append(w3)
        w1, w2 = w2, w3
    return " ".join(result)
random.seed(42)
print("BIGRAM GENERATED TEXT")
print("-" * 30)
for i in range(3):
    print(generate_bigram())
print("\nTRIGRAM GENERATED TEXT")
print("-" * 30)
for i in range(3):
    print(generate_trigram())