a = float(input("Veuillez entrer le premier nombre : "))
b = float(input("Veuillez entrer le deuxième nombre : "))

print(f'La somme : {a} + {b} = {a + b}')
print(f'La différence : {a} - {b} = {a - b}')
print(f'Le produit : {a} * {b} = {a * b}')

if b != 0:
    print(f'La division : {a} / {b} = {a / b}')
else:
    print("La division par zéro n'est pas possible.")
