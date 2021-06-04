from thesaurus.dict import read, guesser, data


def driver():
    word = input("Enter word: ")

    if word.lower() in data:
        return read(word.lower())
    elif word.title() in data:
        return read(word.title())
    elif word.upper() in data:
        return read(word.upper())
    else:
        print(f"The word \"{word}\" was not found.")
        return guesser(word)


print(driver())
