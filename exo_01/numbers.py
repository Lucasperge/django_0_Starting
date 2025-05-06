# Ouvre le fichier numbers.txt en mode lecture
with open("numbers.txt", "r") as fichier:
    contenu = fichier.read()  # lit le contenu du fichier

# Sépare les nombres là où il y a des virgules
nombres = contenu.split(",")

# Affiche chaque nombre sur une ligne
for nombre in nombres:
    print(nombre)
