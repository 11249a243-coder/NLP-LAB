import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The teacher explains the lesson in the classroom."

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<NN.*>+}
    PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)
result = chunker.parse(tagged)

print("POS Tagged Sentence:")
print(tagged)

print("\nChunked Sentence:")
print(result)
result.pretty_print()