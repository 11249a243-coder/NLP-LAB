text = "The cat sat on the mat. The dog sat on the log."

words = text.replace(".", "").split()

lower_words = [w.lower() for w in words]

tokens = len(words)
types_lower = len(set(lower_words))
types_case = len(set(words))

ttr = types_lower / tokens

print("Tokens:", tokens)
print("Lowercase Types:", types_lower)
print("Case Preserved Types:", types_case)
print("TTR:", round(ttr, 2))