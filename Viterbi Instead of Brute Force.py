tags = 45
words = 20

brute_force = tags ** words
viterbi = words * tags ** 2

print("Number of Tags:", tags)
print("Number of Words:", words)
print("Brute Force Sequences:", brute_force)
print("Viterbi Operations:", viterbi)