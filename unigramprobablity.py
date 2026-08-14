import re
import nltk
from nltk.probability import FreqDist

nltk.download("punkt")

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

tokens = re.findall(r"[a-z']+", corpus.lower())

freq_dist = FreqDist(tokens)
N = len(tokens)

print("Total tokens:", N)
print(f"{'Word':<12}{'Count':<8}{'P(word)':<10}")
print("-" * 30)

for word, count in freq_dist.most_common():
    probability = count / N
    print(f"{word:<12}{count:<8}{probability:<10.4f}")

word = "fox"
print(f"\nP('{word}') = {freq_dist[word] / N:.4f}")