import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

sentence = "The very intelligent student reads a book"

words = word_tokenize(sentence)
tagged_words = pos_tag(words)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
"""

chunker = RegexpParser(grammar)
result = chunker.parse(tagged_words)

print("Tagged Words:")
print(tagged_words)

print("\nChunked Output:")
print(result)

print("\nImproved Grammar:")
improved_grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""

improved_chunker = RegexpParser(improved_grammar)
improved_result = improved_chunker.parse(tagged_words)

print(improved_result)