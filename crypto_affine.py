# -*- coding: utf-8 -*-
"""
NOM COMPLET: KAZINGUFU ZABILO MARCELIN

L3 LMD/MSI

QUESTION 2: IMPLEMENTER LE CYPTO SYSTEME D'AFFINE

"""
def crypto_affine (texte_plain: str, K1:int, K2: int) -> str:
    
    texte_plain = texte_plain.upper()
    
    texte_chiffre = ""
    
    for i in texte_plain:
        
        if i.isalpha():
            
            value = (K1 *  (ord (i) - 65) + K2) % 26
            
            texte_chiffre += chr (value + 65)
            
        else:
            
            texte_chiffre += i
            
    return texte_chiffre

# EXEMPLE

texte_plain = input("entrer le mot à crypter en affine:")

K1 = int(input("entrer la valeur de K1:"))

K2 = int(input("entrer la valeur de K2:"))

texte_chiffre = crypto_affine (texte_plain, K1, K2)

print (f"plain text: {texte_plain}")

print (f"cle: K1= {K1}, K2= {K2}")

print (f"cipher text: {texte_chiffre}")
