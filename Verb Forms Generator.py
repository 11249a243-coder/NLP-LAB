words = [
    ("write", "VBD"),
    ("write", "VBN"),
    ("stop", "VBG"),
    ("study", "VBZ"),
    ("die", "VBG"),
    ("play", "VBD")
]

forms = {
    ("write", "VBD"): "wrote",
    ("write", "VBN"): "written",
    ("stop", "VBG"): "stopping",
    ("study", "VBZ"): "studies",
    ("die", "VBG"): "dying",
    ("play", "VBD"): "played"
}

for word, tag in words:
    print(word, tag, "->", forms[(word, tag)])