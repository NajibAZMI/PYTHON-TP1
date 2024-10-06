import sys
if (len(sys.argv)>1):
         prenom=sys.argv[1]   ;   
else:     
        prenom=input("Entrer Votre Prenom:")
print(f'Bonjour,[{prenom}]')