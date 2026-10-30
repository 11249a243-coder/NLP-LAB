
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import brown
from nltk import UnigramTagger

nltk.download('brown')

print("Ambiguity Problem")

sentence1 = "I saw her duck under the table and duck the flying ball."
print(pos_tag(word_tokenize(sentence1)))

print("\nUnknown Word Problem")

sentence2 = "Ravi uses Zorblax technology."
print(pos_tag(word_tokenize(sentence2)))

print("\nDomain Dependence")

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

tagger = UnigramTagger(train_data)

sentence3 = "Wow LOL this movie is amazing."
sentence4 = "The stars are dancing in the silent sky."

print(tagger.tag(word_tokenize(sentence3)))
print(tagger.tag(word_tokenize(sentence4)))
