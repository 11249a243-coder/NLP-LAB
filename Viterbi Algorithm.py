words = ["the", "dog", "barks"]
tags = ["D", "N", "V"]

trans = {
    ("<s>", "D"): 0.6,
    ("<s>", "N"): 0.3,
    ("<s>", "V"): 0.1,
    ("D", "D"): 0.05,
    ("D", "N"): 0.9,
    ("D", "V"): 0.05,
    ("N", "D"): 0.2,
    ("N", "N"): 0.2,
    ("N", "V"): 0.6,
    ("V", "D"): 0.6,
    ("V", "N"): 0.3,
    ("V", "V"): 0.1
}

emit = {
    ("the", "D"): 0.7,
    ("dog", "N"): 0.3,
    ("dog", "V"): 0.01,
    ("barks", "N"): 0.1,
    ("barks", "V"): 0.2
}

dp = []
path = []

first = {}

for tag in tags:
    first[tag] = trans[("<s>", tag)] * emit.get((words[0], tag), 0)

dp.append(first)
path.append({tag: None for tag in tags})

for word in words[1:]:
    current = {}
    back = {}

    for tag in tags:
        values = [
            dp[-1][prev] * trans[(prev, tag)] *
            emit.get((word, tag), 0)
            for prev in tags
        ]

        best = max(values)
        current[tag] = best

        if best > 0:
            back[tag] = tags[values.index(best)]
        else:
            back[tag] = None

    dp.append(current)
    path.append(back)

best_tag = max(tags, key=lambda t: dp[-1][t])

result = [best_tag]

for i in range(len(words)-1, 0, -1):
    best_tag = path[i][best_tag]
    result.append(best_tag)

result.reverse()

print("Words:", words)
print("Best Tags:", result)
print("Probability:", dp[-1][result[-1]])