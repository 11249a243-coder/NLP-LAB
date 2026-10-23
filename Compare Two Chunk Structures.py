import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "a student",
    "the very intelligent student"
]

grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    result = chunker.parse(tagged)

    print("\nSentence:", sentence)
    print("POS Tags:", tagged)
    print("Chunk Structure:")
    print(result)