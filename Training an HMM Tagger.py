from collections import Counter, defaultdict

sentences = [
    [("the", "D"), ("dog", "N"), ("barks", "V")],
    [("a", "D"), ("cat", "N"), ("sleeps", "V")],
    [("dogs", "N"), ("bark", "V")],
    [("the", "D"), ("cat", "N"), ("chases", "V"),
     ("the", "D"), ("dog", "N")]
]

transitions = Counter()
emissions = Counter()
tag_counts = Counter()

for s in sentences:
    previous = "<s>"

    for word, tag in s:
        transitions[(previous, tag)] += 1
        emissions[(tag, word)] += 1
        tag_counts[tag] += 1
        previous = tag

    transitions[(previous, "</s>")] += 1

print("Transition Probabilities:")

for pair in [("<s>", "D"), ("D", "N"),
             ("N", "V"), ("V", "</s>")]:
    if pair[0] == "<s>":
        total = len(sentences)
    elif pair[1] == "</s>":
        total = sum(1 for s in sentences if s[-1][1] == pair[0])
    else:
        total = sum(v for (a, b), v in transitions.items() if a == pair[0])

    print(pair, ":", transitions[pair] / total)

print("\nEmission Probabilities:")
print("P(the|D):", emissions[("D", "the")] / tag_counts["D"])
print("P(cat|N):", emissions[("N", "cat")] / tag_counts["N"])
print("P(barks|V):", emissions[("V", "barks")] / tag_counts["V"])