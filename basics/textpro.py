def sentence_maker(phrase):
    phrase = phrase.capitalize()
    interrogatives = ("Are", "How", "What", "Why", "Where", "When", "Who")

    if phrase.startswith(interrogatives):
        return f"{phrase}?"
    else:
        return f"{phrase}."


phrases = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        phrases.append(sentence_maker(user_input))

print(" ".join(phrases))
