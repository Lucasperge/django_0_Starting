def all_in():

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    import sys

    if len(sys.argv) != 2:
        sys.exit()

    # On récupère l'entrée, on la sépare par virgule et on nettoie les espaces
    inputs = [item.strip() for item in sys.argv[1].split(',')]

    for word in inputs:
    # On normalise la casse (première lettre en majuscule, le reste en minuscule)
        word = word.title()

        if word in states:
            abbr = states[word]
            capital = capital_cities.get(abbr)
            if capital:
                print(f"{capital} is the capital of {word}")
        elif word in capital_cities.values():
            abbr = [key for key, val in capital_cities.items() if val == word][0]
            state = [key for key, val in states.items() if val == abbr][0]
            print(f"{word} is the capital of {state}")
        else:
            print(f"{word} is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()
