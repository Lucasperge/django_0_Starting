def capital_city():

    import sys

# Les dictionnaires
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

# Vérifier si le nombre d'arguments est exactement 2
    if len(sys.argv) != 2:
        exit()  # Si le nombre d'arguments n'est pas correct, on quitte le programme

# Récupérer le nom de l'état passé en argument
    state_name = sys.argv[1]

# Vérifier si l'état est dans le dictionnaire 'states'
    if state_name in states:
        state_abbr = states[state_name]  # Obtenir l'abréviation de l'état
        print(capital_cities[state_abbr])  # Afficher la capitale correspondante
    else:
        print("Unknown state")  # Si l'état n'est pas trouvé, afficher "Unknown state"

if __name__ == '__main__':
    capital_city()