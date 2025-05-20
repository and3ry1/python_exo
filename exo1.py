number = int(input("ecrit un nombre: "))

if number > 0:
    print('positif')
elif number < 0:
    print('negatif')
else:
    print('nul')



# demande d'écrire un autre nombre
number2 = int(input("ecrit un autre nombre: "))

if number2 > 0:
    print('positif')
elif number2 < 0:
    print('negatif')
else:
    print('nul')

# compare les deux nombres
if number > number2:
    print (number)

elif number < number2:
    print (number2) 

else:
    print("les deux nombres sont egaux")    


        
if number > 18:
    print("majeur")

elif number < 18:
    print("mineur") 
else:
    print("vous avez 18 ans")

