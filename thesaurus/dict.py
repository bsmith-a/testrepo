from difflib import get_close_matches
import json

data = json.load(open("data.json"))


def read(key):
    return "\n".join(data[key])


def guesser(g):
    guess_list = []
    if len(get_close_matches(g, data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g, data.keys(), cutoff=0.8))
    if len(get_close_matches(g.title(), data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g.title(), data.keys(), cutoff=0.8))
    if len(get_close_matches(g.upper(), data.keys(), cutoff=0.8)) > 0:
        guess_list.append(get_close_matches(g.upper(), data.keys(), cutoff=0.8))

    for guess in guess_list:
        for g in guess:
            yn = input(f"Did you mean {g}? Enter Y/N: ").upper()
            if yn == "Y":
                return read(g)
            elif yn != "N":
                return "Wrong input."

    return "Word not found. Check spelling and try again."
