import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    result = chunker.parse(tagged)

    print("\nSentence:", sentence)
    print(result)