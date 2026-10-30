
import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r".*'s$", 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),
    (r'(The|the|A|a|An|an)$', 'DT'),
    (r'(in|on|at|of|for|with)$', 'IN'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged = tagger.tag(tokens)

print("\nWord\t\tPoS Tag")
print("-" * 30)

for word, tag in tagged:
    print(f"{word}\t\t{tag}")
