
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]

for sentence in sentences:
    print("\nSentence:", sentence)
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)

    for word, tag in tags:
        print(word, "-", tag)
