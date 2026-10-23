import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The teacher explains the lesson in the classroom."

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

grammar_np = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

grammar_all = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
    VP: {<VB.*><NP|PP>*}
"""

chunker_np = nltk.RegexpParser(grammar_np)
chunker_all = nltk.RegexpParser(grammar_all)

result_np = chunker_np.parse(tagged)
result_all = chunker_all.parse(tagged)

print("POS Tags:")
print(tagged)

print("\nNP Only:")
print(result_np)

print("\nNP + VP + PP:")
print(result_all)