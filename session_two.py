# Exercice:
# Écrire un programme python qui vous permet de convertir du Fahrenheit au Celsius et vis versa
# PS:
# Faudrait résoudre en utilisant les conditions et les boucles
# --------------------------------------condition------------------------------------------------
temp = input("Entrez la température que vous souhaitez convertir (par exemple, 45, 102, etc.): ")   #45
unit = input("De quelle unité de temperature s'agit-il ?")

degree = int(temp)  # nous essayons de le convertir en entier

if unit.upper() == "C":
    pre_result_without_round = (9 * degree) / 5 + 32
    pre_result_with_round = round(pre_result_without_round)     #round(number, digits)   التدوير الي الوحدة
    result = int(pre_result_with_round)
    unit_convention = "Fahrenheit"
elif unit.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    unit_convention = "Celsius"
else:
    print("Entrez la convention appropriée.")
    quit()   #quitter le programme emediatement sans continuer le reste

print ("La température en", unit_convention, "est", result, "degrés.")






# --------------------------------------pour------------------------------------------------
valeurs_str = input("Combien de valeurs souhaitez-vous convertir?")
valeurs = int(valeurs_str)

for i in range(valeurs):      #range(start, end, steps)

    temp = input("Entrez la température que vous souhaitez convertir? (par exemple, 45, 102, etc.): ")   #45
    unit = input("De quelle unité de temperature s'agit-il ?")
    degree = int(temp)

    if unit.upper() == "C":
        pre_result_without_round = (9 * degree) / 5 + 32
        pre_result_with_round = round(pre_result_without_round)     #round(number, digits)   التدوير الي الوحدة
        result = int(pre_result_with_round)
        unit_convention = "Fahrenheit"
    elif unit.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        unit_convention = "Celsius"
    else:
        print("Entrez la convention appropriée.")
        quit()   #quitter le programme emediatement sans continuer le reste

    print("La température en", unit_convention, "est", result, "degrés.")

# -----------------------------------------------tant que---------------------------------------------------------
valeurs_str = input("Combien de valeurs souhaitez-vous convertir?")
valeurs = int(valeurs_str)

i = 0 # ou i = int()

while i < valeurs:
    temp = input("Entrez la température que vous souhaitez convertir? (par exemple, 45, 102, etc.): ")   #45
    unit = input("De quelle unité de temperature s'agit-il ?")

    degree = int(temp)

    if unit.upper() == "C":
        pre_result_without_round = (9 * degree) / 5 + 32
        pre_result_with_round = round(pre_result_without_round)     #round(number, digits)   التدوير الي الوحدة
        result = int(pre_result_with_round)
        unit_convention = "Fahrenheit"
    elif unit.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        unit_convention = "Celsius"
    else:
        print("Entrez la convention appropriée.")
        quit()   #quitter le programme emediatement sans continuer le reste

    print("The temperature in", unit_convention, "is", result, "degrees.")
    i = i + 1 # incrementation


# -------------------------------------------repeter-------------------------------------------------------------
valeurs_str = input("Combien de valeurs souhaitez-vous convertir?")
valeurs = int(valeurs_str)

i = 0 # ou i = int()

while True:
    temp = input("Entrez la température que vous souhaitez convertir? (par exemple, 45, 102, etc.): ")   #45
    unit = input("De quelle unité de temperature s'agit-il ?")

    degree = int(temp)

    if unit.upper() == "C":
        pre_result_without_round = (9 * degree) / 5 + 32
        pre_result_with_round = round(pre_result_without_round)     #round(number, digits)   التدوير الي الوحدة
        result = int(pre_result_with_round)
        unit_convention = "Fahrenheit"
    elif unit.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        unit_convention = "Celsius"
    else:
        print("Entrez la convention appropriée.")
        quit()   #quitter le programme emediatement sans continuer le reste

    print("The temperature in", unit_convention, "is", result, "degrees.")
    i = i + 1
    if i >= valeurs:
        print(i)
        break


# remmarques :
# L’instruction "break" permet de « casser » l’exécution d’une boucle (while ou for). Elle fait sortir de la boucle et passer à l’instruction suivante.
# L’instruction "continue" permet de passer prématurément au tour de boucle suivant. Elle fait continuer sur la prochaine itération de la boucle.
