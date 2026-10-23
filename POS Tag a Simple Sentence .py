import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "Ravi plays cricket every evening."

tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

print("Word\tPOS Tag")
print("-" * 25)

for word, tag in tags:
    print(word, "\t", tag)