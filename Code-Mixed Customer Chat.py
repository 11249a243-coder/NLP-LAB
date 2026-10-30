text = "Kal ka meeting cancel ho gaya please reschedule it by Friday"

hindi = ["Kal", "ka", "ho", "gaya"]

words = text.split()

for word in words:
    if word in hindi:
        print(word, "- Hindi")
    else:
        print(word, "- English")