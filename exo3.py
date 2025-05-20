#demande a l'ordinateur d'écrire un nombre aléatoire entre 1 et 100
import random
number = (random.randint(1, 100))

print(number)

#demande à l'utilisateur d'écrire un nombre
number2 = int(input("ecrit un nombre: "))

#compare les deux nombres
if number2 > number:
    print(f"{number2} est plus grand") 

elif number2 < number:
    print(f"{number2} est plus petit") 

else:
    print("les deux nombres sont egaux") 

#boucle pour saisir un autre nombre

while number != number2:
    number2 = int(input("ecrit un autre nombre: "))
    if number2 > number:
        print(f"{number2} est plus grand") 

    elif number2 < number:
        print(f"{number2} est plus petit")

    else:
        print("les deux nombres sont egaux")
