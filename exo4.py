#gestion de mot de passe
password = input("saisir un mot de passe:" )


#vérifie si le mot de passe contient au moins 8 caractères
nombre_de_mots = len(password)
if nombre_de_mots < 8:

    print("le mot de passe doit contenir au moins 8 caractères")

#vérifie si le mot de passe contient au moins une lettre majuscule

if password.islower():
    print("le mot de passe doit contenir au moins une lettre majuscule")    

#vérifie si le mot de passe contient un chiffre

if password.isalpha():
    print("le mot de passe doit contenir au moins un chiffre")

while password.isalpha() or password.islower() or nombre_de_mots < 8:
    password = input("saisir un mot de passe:" )
    nombre_de_mots = len(password)
    if nombre_de_mots < 8:
        print("le mot de passe doit contenir au moins 8 caractères")
    if password.islower():
        print("le mot de passe doit contenir au moins une lettre majuscule")    
    if password.isalpha():
        print("le mot de passe doit contenir au moins un chiffre")

else :
    print("connexion ok")
    exit()

    