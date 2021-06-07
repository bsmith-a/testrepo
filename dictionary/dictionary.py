import mysql.connector
from difflib import get_close_matches

# connects to database
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

# creates cursor to navigate through database
cursor = con.cursor()

# gets user input
word = input("Enter a word: ")

# gets all results from dictionary matching word entered
query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}' ")
results = cursor.fetchall()


# finds close matches to misspelled word
def guesser(w):
    print("Word not found.")

    # stores all expressions in the dictionary starting with the first letter of the word in r
    # r is a list of tuples containing one value
    letter = w[0]
    q = cursor.execute(f"SELECT Expression FROM Dictionary WHERE Expression REGEXP '^[{letter}].*$'")
    r = cursor.fetchall()

    # creates a list of strings from r and excluding duplicates
    guess_list = []
    for val in r:
        for v in val:
            if v not in guess_list:
                guess_list.append(v)

    # finds all close matches in the list r
    guesses = get_close_matches(w, guess_list, cutoff=0.8)

    # asks the user if they meant to type any of the words in guesses
    # returns definition(s) if user enters Y
    for g in guesses:
        yn = input(f"Did you mean {g}? Enter Y/N: ").upper()
        if yn == "Y":
            # gets definition for word accepted
            que = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{g}' ")
            res = cursor.fetchall()
            for definition in res:
                for defs in definition:
                    print("".join(defs))
            return ""
        elif yn != "N":
            return "Wrong input."

    # returns this if no similar matches are found or if user declines all guesses
    return "Word not found. Check spelling and try again."


# if result found, print definition(s), else go to guesser
if results:
    for result in results:
        print(result[1])
else:
    print(guesser(word))
