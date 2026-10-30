
import nltk
import numpy as np
from nltk.corpus import brown
from nltk.tag import hmm

hmm.np = np

nltk.download('brown')

data = brown.tagged_sents(categories='news')

size = int(len(data) * 0.9)
train_data = data[:size]
test_data = data[size:]

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

accuracy = tagger.accuracy(test_data)

print("HMM Tagger Accuracy:", round(accuracy * 100, 2), "%")

sentence = ["They", "refuse", "to", "permit", "the", "strike"]

result = tagger.tag(sentence)

print("\nInput Sentence:", sentence)
print("Tagged Output:", result)
