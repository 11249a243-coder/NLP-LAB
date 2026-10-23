import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The young researcher develops an AI model."

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)
result = chunker.parse(tagged)

print("POS Tagged Sequence:")
print(tagged)

print("\nNoun Phrases:")
print(result)
result.pretty_print()