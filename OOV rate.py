import re

training_text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

test_sentence = "the clever fox jumps over the cat"

def tokenize(text):
    return re.findall(r"[a-z']+", text.lower())

training_tokens = tokenize(training_text)
test_tokens = tokenize(test_sentence)

training_vocabulary = set(training_tokens)

def oov_rate(test_tokens, vocabulary):
    if not test_tokens:
        return 0.0

    oov_words = [
        word for word in test_tokens
        if word not in vocabulary
    ]

    return len(oov_words) / len(test_tokens)

rate = oov_rate(test_tokens, training_vocabulary)

print("Test sentence:", test_sentence)
print("Test tokens:", len(test_tokens))
print("OOV words:", [
    word for word in test_tokens
    if word not in training_vocabulary
])
print(f"OOV Rate: {rate:.4f}")
print(f"OOV Percentage: {rate * 100:.2f}%")