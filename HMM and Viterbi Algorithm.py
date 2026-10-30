
start_p = {
    'DT': 0.6,
    'NN': 0.3,
    'VB': 0.1
}

trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}

emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}

words = ['a', 'cat', 'runs']
states = ['DT', 'NN', 'VB']

V = [{}]
path = {}

for state in states:
    V[0][state] = start_p[state] * emit_p[state].get(words[0], 0)
    path[state] = [state]

print("Initialization:")
print(V[0])

for t in range(1, len(words)):
    V.append({})
    new_path = {}

    for state in states:
        probabilities = []

        for previous in states:
            value = (
                V[t-1][previous]
                * trans_p[previous][state]
                * emit_p[state].get(words[t], 0)
            )
            probabilities.append((value, previous))

        best_probability, best_previous = max(probabilities)

        V[t][state] = best_probability
        new_path[state] = path[best_previous] + [state]

    path = new_path

best_state = max(V[-1], key=V[-1].get)
print("\nViterbi Probabilities:")
for row in V:
    print(row)

print("\nBest Tag Sequence:")
print(path[best_state])

print("\nFinal Probability:")
print(V[-1][best_state])
