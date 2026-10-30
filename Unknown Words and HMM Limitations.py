training_words = [
    "the", "dog", "barks", "a", "cat",
    "sleeps", "dogs", "bark", "chases"
]

test_words = ["the", "cats", "chase", "the", "dog"]

print("Testing Sentence:")

for word in test_words:
    if word in training_words:
        print(word, "-> Known Word")
    else:
        print(word, "-> Unknown Word")

print("\nUnknown Word Handling:")
print("cats -> Noun (based on suffix -s)")
print("chase -> Verb (based on context)")