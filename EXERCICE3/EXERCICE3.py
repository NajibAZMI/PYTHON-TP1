import datetime
nom=input("Entrer Votre Nom :")
age=int(input("Veuillez Entrer Votre age :"))
date_Aujourdhui=int(datetime.datetime.now().year)
date_80=date_Aujourdhui+80-age
print(f'Bonjour {nom}({age}), tu auras 80 l\’année : {date_80}')