import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The student reads a book in the library.",
    "The professor teaches computer science.",
    "The students play football on the ground.",
    "A researcher develops an AI model in the laboratory.",
    "The principal attends a meeting in the office."
]

grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
    VP: {<VB.*><NP|PP>*}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    result = chunker.parse(tagged)

    print("\nSentence:", sentence)
    print("Chunk Tree:")
    print(result)