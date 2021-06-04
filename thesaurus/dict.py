from difflib import get_close_matches
import json

# loads dictionary file as dictionary data type
data = json.load(open("data.json"))


# prints out each definition for a word on separate lines
def read(key):
    return "\n".join(data[key])


# finds close matches for misspelled words
def guesser(g):
    guess_list = []
    # checks for similar words in dictionary
    if len(get_close_matches(g, data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g, data.keys(), cutoff=0.8))
    # checks for similar proper nouns in dictionary
    if len(get_close_matches(g.title(), data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g.title(), data.keys(), cutoff=0.8))
    # checks for similar acronyms in dictionary
    if len(get_close_matches(g.upper(), data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g.upper(), data.keys(), cutoff=0.8))

    # returns each of the guesses in the guess_list and asks user if given guess is correct
    # get_close_matches returns a list so guess_list is a list of lists
    for guess in guess_list:
        for g in guess:
            yn = input(f"Did you mean {g}? Enter Y/N: ").upper()
            if yn == "Y":
                return read(g)
            elif yn != "N":
                return "Wrong input."

    return "Word not found. Check spelling and try again."
