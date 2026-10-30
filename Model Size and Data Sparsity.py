v = 20000
tokens = 10000000

bigrams = v ** 2
trigrams = v ** 3

fraction = tokens / trigrams

print("Vocabulary Size:", v)
print("Possible Bigrams:", bigrams)
print("Possible Trigrams:", trigrams)
print("Maximum Trigram Fraction:", fraction)