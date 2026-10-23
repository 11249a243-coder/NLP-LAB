import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The intelligent student reads a book."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)
result = chunker.parse(tagged_words)

print("Chunked Sentence:")
print(result)

result.pretty_print()