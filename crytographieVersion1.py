def chiffrement_cesar(texte, cle):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texte_chiffre = ""
    texte = texte.upper()

    for c in texte:
        if c.isalpha():
            indice = (alphabet.index(c) + cle) % 26
            caractere_chiffre = alphabet[indice]
            texte_chiffre += caractere_chiffre
        else:
            texte_chiffre += c

    return texte_chiffre

texte_original = input("Entrer un texte ou mot de votre choix ")
cle =int(input("Entrer votre clé "))
texte_chiffre = chiffrement_cesar(texte_original, cle)
print(texte_chiffre)
