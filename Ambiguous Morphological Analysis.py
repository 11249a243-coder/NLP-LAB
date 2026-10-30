analyses = {
    "flies": ["fly + Noun + Plural", "fly + Verb + 3SG"],
    "saw": ["saw + Noun + Singular", "see + Verb + Past"],
    "leaves": ["leaf + Noun + Plural", "leave + Verb + 3SG"]
}

for word, meanings in analyses.items():
    print("\nWord:", word)
    for meaning in meanings:
        print(meaning)