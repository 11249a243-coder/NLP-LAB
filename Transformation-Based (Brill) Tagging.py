
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger
from nltk.tag import brill, brill_trainer

nltk.download('brown')

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

baseline_tagger = UnigramTagger(train_data)

templates = brill.brill24()

trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger,
    templates,
    trace=3
)

print("Baseline Accuracy:")
print(baseline_tagger.accuracy(test_data))

print("\nTraining Brill Tagger with 10 Rules")

brill_tagger = trainer.train(train_data, max_rules=10)

print("Brill Accuracy:")
print(brill_tagger.accuracy(test_data))

print("\nTraining Brill Tagger with 30 Rules")

brill_tagger = trainer.train(train_data, max_rules=30)

print("Brill Accuracy:")
print(brill_tagger.accuracy(test_data))

sentence = "They will fish for hours near the river bank"

tokens = nltk.word_tokenize(sentence)

print("\nTagged Sentence:")
print(brill_tagger.tag(tokens))
