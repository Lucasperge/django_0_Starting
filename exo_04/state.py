def state():

    import sys

# Dictionnaires fournis
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

# Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        exit()  # Quitte si trop ou pas d'arguments

# Récupérer la capitale entrée
    capital_name = sys.argv[1]

# Recherche de l'État en utilisant la capitale
    found = False
    for state_code, capital in capital_cities.items():
        if capital == capital_name:
            state_name = [state for state, code in states.items() if code == state_code][0]
            print(state_name)
            found = True
            break

# Si la capitale n'est pas trouvée
    if not found:
        print("Unknown capital city")

if __name__ == '__main__':
    state()
