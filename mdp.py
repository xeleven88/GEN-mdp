import random
import string

def creemdp(taille):
    if taille < 4:
        print("le mot de passe doit contenir au moins 4 characters")
        return none
    
    lowercase = string.ascii_lowercase  # MINI
    uppercase = string.ascii_uppercase  # MAJ
    digits = string.digits              # NUM
    symbols = "!@#$%^&*()-_=+<>?/|"
    
    choix = (input("Voulez vous des symbole dans votre mdp (oui ou non) ? : ")).lower()

    if choix == "oui":
        mdp = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
            ]
        all_characters = lowercase + uppercase + digits + symbols
    else:
        mdp = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        ]
        all_characters = lowercase + uppercase + digits 
    
    
    mdp += random.choices(all_characters, k=taille - len(mdp))
    
    
    random.shuffle(mdp)
    return ''.join(mdp)

try:
    taille = int(input("Entrez la longueur souhaitée du mot de passe : "))
    mdp = creemdp(taille)
    if mdp:
        print(f"Mot de passe généré : {mdp}")
except ValueError:
    print("Veuillez entrer un nombre valide.")