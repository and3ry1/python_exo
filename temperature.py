def temperature():
# demande utilisateur d'ecrire un nombre
        
    print("ceci est un programme qui permet de convertir les unités de temperatures")

    number = input("ecrit un nombre: ")
    while not number.isdigit():     
        number = input("ecrire un nombre:")


# demande utilisateur d'ecrire l'unité de temperature
    temperature = ['F' , 'C', 'K']

    unite1 = input("quel unité de mesure ?: ")

    while unite1 not in temperature:
    
        unite1 = input("mettre unité de mesure valide:")

# ecrire automatiquement number + unité
    else:

        valeur_1 = number + unite1    
    

# demande utilisateur quel unité de conversion il souhaites 
    convert = ['F' , 'C', 'K']

    unite2 = input (f"{valeur_1} vers quel unité ? :")

    while unite2 not in convert:
                    
        unite2 = input("mettre une autre unité de mesure :")

    while unite1 == unite2:
        unite2 = input("mettre une autre unité de mesure :")

#calcul de conversion par des conditions 


#F --> C (C = (F − 32) × 5 ÷ 9)
    if unite1 == "F" and unite2 == "C":
        print (f"{(float(number) - 32) * 5 /9} °{unite2}")

#invert C-->F (F = (C × 9/5) + 32)
    if unite1 == "C" and unite2 == "F":
        print (f"{(float(number) *9/5 )+32} °{unite2}")


# F--> K (K= (F + 459.67) * 5/9)
    if unite1 == "F" and unite2 == "K":
        print (f"{(float(number)+ 459.67)*5/9} °{unite2}")
#invert K --> F (F= (K * 9/5)-459.67)
    if unite1 == "K" and unite2 == "F":
        print (f"{(float(number)*9/5)- 459.67} °{unite2} ")
 

 # C --> K  (K = C + 273.15)
    if unite1 == "C" and unite2 =="K":
        print (f"{(float(number)+ 273.15)} °{unite2} ")
 # invert K --> C (C = K -273.15)
    if unite1 == "K" and unite2 =="C":
        print (f"{(float(number)-273.15)} °{unite2}")
 

 #Boucle
while True :
    temperature()
    again = input("souhaites tu faire une autre conversion ? oui ou non :")
    
    if again != "oui":
  
        print ("bonne journée")
        break

