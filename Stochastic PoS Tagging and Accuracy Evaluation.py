
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger

nltk.download('brown')

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

print("90% Training Data")
print("Unigram Accuracy:", unigram_tagger.accuracy(test_data))
print("Bigram Accuracy:", bigram_tagger.accuracy(test_data))

size = int(len(tagged_sentences) * 0.5)

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

print("\n50% Training Data")
print("Unigram Accuracy:", unigram_tagger.accuracy(test_data))
print("Bigram Accuracy:", bigram_tagger.accuracy(test_data))

tagged_sentences = brown.tagged_sents(categories='romance')

size = int(len(tagged_sentences) * 0.9)

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

print("\nRomance Category")
print("Unigram Accuracy:", unigram_tagger.accuracy(test_data))
print("Bigram Accuracy:", bigram_tagger.accuracy(test_data))

