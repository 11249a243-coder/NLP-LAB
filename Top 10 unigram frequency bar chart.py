import re
import nltk
import matplotlib.pyplot as plt
from collections import Counter

nltk.download("gutenberg")

text = nltk.corpus.gutenberg.raw("austen-emma.txt")

tokens = re.findall(r"[a-z']+", text.lower())

unigram_counts = Counter(tokens)

top10 = unigram_counts.most_common(10)

words = [word for word, count in top10]
counts = [count for word, count in top10]

plt.figure(figsize=(10, 6))

plt.bar(words, counts, color="skyblue")

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigrams in Emma")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

