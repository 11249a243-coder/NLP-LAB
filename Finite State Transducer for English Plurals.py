words = ["fox", "cat", "church", "wish", "boy"]

for word in words:
    if word.endswith(("x", "s", "z", "ch", "sh")):
        plural = word + "es"
    else:
        plural = word + "s"

    print(word, "->", plural)