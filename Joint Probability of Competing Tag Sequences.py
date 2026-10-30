transitions = {
    ("<s>", "D"): 0.6,
    ("D", "N"): 0.9,
    ("N", "V"): 0.6,
    ("N", "N"): 0.2
}

emissions = {
    ("the", "D"): 0.7,
    ("dog", "N"): 0.3,
    ("dog", "V"): 0.01,
    ("barks", "N"): 0.1,
    ("barks", "V"): 0.2
}

p1 = 0.6 * 0.7 * 0.9 * 0.3 * 0.6 * 0.2
p2 = 0.6 * 0.7 * 0.9 * 0.3 * 0.2 * 0.1

print("Probability of D N V:", p1)
print("Probability of D N N:", p2)
print("Preferred Sequence: D N V")
print("Factor:", p1 / p2)