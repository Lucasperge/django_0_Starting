def periodic_table() :

# Ouvrir et lire le fichier contenant les éléments chimiques
    with open('periodic_table.txt', 'r') as file:
        lines = file.readlines()

# Création d'un dictionnaire pour placer les éléments par ligne et colonne
table = [[None] * 18 for _ in range(7)]  # 7 lignes et 18 colonnes dans le tableau de Mendeleïev

# Traitement des éléments et placement dans le tableau
for element in elements:
    # Sépare les données et récupère les informations
    element_info = [item.strip().split(":")[1].strip() for item in element.strip().split(",")]
    
    if len(element_info) == 4:  # Si les informations sont complètes
        name, position, number, molar = element_info
        position = int(position)
        
        # Calcule la ligne et la colonne pour placer l'élément
        row = position // 18
        col = position % 18
        
        # Place l'élément dans le tableau
        table[row][col] = (name, number, molar)

# Création du fichier HTML
with open("periodic_table.html", "w") as html_file:
    html_file.write("<html><head><title>Periodic Table</title><style>")
    html_file.write("table { border-collapse: collapse; }")
    html_file.write("td, th { padding: 10px; border: 1px solid black; text-align: center; }")
    html_file.write("th { background-color: #f2f2f2; font-weight: bold; }")
    html_file.write("</style></head><body>")
    html_file.write("<h1>Periodic Table of Elements</h1>")
    html_file.write("<table>")

    # Ajoute les entêtes du tableau
    html_file.write("<tr>")
    for i in range(18):  # 18 colonnes
        html_file.write(f"<th>Column {i + 1}</th>")
    html_file.write("</tr>")

    # Remplissage du tableau avec les éléments
    for row in table:
        html_file.write("<tr>")
        for element in row:
            if element is None:
                html_file.write("<td></td>")  # Cellule vide
            else:
                name, number, molar = element
                html_file.write("<td>")
                html_file.write(f"<h4>{name}</h4>")
                html_file.write("<ul>")
                html_file.write(f"<li>Number: {number}</li>")
                html_file.write(f"<li>Molar Mass: {molar}</li>")
                html_file.write("</ul>")
                html_file.write("</td>")
        html_file.write("</tr>")
    
    html_file.write("</table></body></html>")

    if __name__ == '__main__':
        periodic_table()
        