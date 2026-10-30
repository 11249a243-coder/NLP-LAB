words = ["box", "city", "child", "boy", "bus", "knife"]

irregular = {
    "child": "children",
    "knife": "knives"
}

for word in words:
    if word in irregular:
        plural = irregular[word]
    elif word.endswith(("s", "x", "z", "ch", "sh")):
        plural = word + "es"
    elif word.endswith("y") and word[-2] not in "aeiou":
        plural = word[:-1] + "ies"
    else:
        plural = word + "s"

    print(word, "->", plural)