import math

list1 = [4, 5, 8, 9, 235, 1712, 230]
for x in list1:
    print(f'Les diviseurs de {x} sont :', end=" ")
    print("[", end=" ")
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            print(i, end=" ")
            if i != x // i:  # Pour éviter d'afficher deux fois le même diviseur
                print(x // i, end=" ")
    print("]")
