
import nltk
from nltk import word_tokenize, pos_tag

sentence = "The little girl quickly finished her homework before dinner."

tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

for word, tag in tagged:
    print(word, "->", tag)

print("\nSimple Sentence:")
sentence2 = "Ravi plays cricket every evening."
print(pos_tag(word_tokenize(sentence2)))

print("\nAmbiguous Sentence:")
sentence3 = "I read a book and watch a movie."
print(pos_tag(word_tokenize(sentence3)))
