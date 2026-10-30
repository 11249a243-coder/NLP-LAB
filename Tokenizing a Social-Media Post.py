import nltk
from nltk.tokenize import TweetTokenizer

text = "OMG!! Can't wait for #NLP2026 @IITM :) Tickets cost $4.5k, e-mail me at ravi@example.com"

tokenizer = TweetTokenizer()
tokens = tokenizer.tokenize(text)

print("Tokens:")
print(tokens)