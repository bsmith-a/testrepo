from thesaurus.dict import read, data, guesser

def driver():
    # asks for word
    word = input("Enter word: ")

    # checks if word is in dictionary
    if word.lower() in data:
        return read(word.lower())
    # checks if word is a proper noun in dictionary
    elif word.title() in data:
        return read(word.title())
    # checks if word is an acronym in dictionary
    elif word.upper() in data:
        return read(word.upper())
    # goes to the guesser method to find intended word
    else:
        print(f"The word \"{word}\" was not found.")
        return guesser(word)


# runs program and prints output
print(driver())
