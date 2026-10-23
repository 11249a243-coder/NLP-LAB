
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "I read a book.",
    "Please book a ticket.",
    "Children play football.",
    "We watched a play."
]

for sentence in sentences:
    print("\nSentence:", sentence)
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)

    for word, tag in tags:
        if word.lower() in ["book", "play", "watch", "watched"]:
            print(word, "-", tag)
