# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:12:24 2022

CE MODULE EST LE POINT DE DEPART DE NOTRE PROGRAMME. C'EST LE CHEF D'ORCHESTRE !

@author: user
"""

from sympy import Matrix
from generatrice  import Gfilling_forced,Gfilling_forced2
from generationcode import code,controle,wordincode
import numpy as np

"""
lors de l'affichage des matrices à l'ecran, convertir tous les types matrix en np.array()
de meme il est preferable d opter pour matrix.tolist() or np.array() pour l'affichage'
"""

def presentation():
    
    # Dialogue d'entrée
    print("BONJOUR ! BIENVENUE DANS NOTRE PROGRAMMME \nL'IMPLEMENTATION C'EST LE DÉCODAGE PAR ENSEMBLE D'INFORMATION ! \n")
    name=(input("Veuillez entrer votre nom svp : ")).upper()
    print("Bonjour M/Mme {}".format(name))
    
    #saisie des parametres k et n valides
    convertion_test=True
    while convertion_test:
        n=input("Veuillez entrer la longueur (valeur de n) du message arrivé : ")
        k=input("Veuillez entrer la longueur (valeur de k) du message de départ : ")
        try:
            n=int(n)
            k=int(k)
            convertion_test=False
            print("Données enregistrées ! Merci !\n ")
        except:
            print("Votre entrée n'est pas valide ! Veuillez recommencer ! ")
            
    #saisi du mot à encoder, message est le mot comportant des erreurs.
    boolean=True
    while boolean:
        l=True;
        while l:             #forcer l'utilisateur à entrer un mot de n bits
            message=list(input("Entrez alors le mot à décoder ( une suite de {} bits ) svp : ".format(n)))
            if len(message)==n:
                l=False
            else:
                print("La longueur de votre mot  n'est pas celle attendue ! Veuillez recommencer !")
            #message=message.split(",") 
        boolean=False
        for i in range(n):
            try:
                message[i]=int(message[i])
                if message[i]!=0 and message[i]!=1:
                    boolean=True
                    print("Votre entrée ne contient pas que  des bits (0 ou 1). Veuillez reprendre ! ")
                    break
            except:
                print("Votre entrée n'est pas valide !  Veuillez recommencer ! ")
                boolean=True
                break
    #--------------------lancement du programmme-----------------------------------------                 
    reponse_user=input("\nComment souhaitez-vous entrer les coefficients de votre matrice génératrice?\nSi à l'aide d'un séparateur entrer OUI/YES sinon NON/NO : ")
    if reponse_user in ["yes","oui","YES","OUI","O","o","y","Y"]:
        symbol=input("Veuillez entrer le séparateur : ")
        G=Gfilling_forced(k, n,symbol)               
        CODE=code(k,G)                
    else:
        print("Vous avez choisi de ne pas entrer les coefficients de chaque ligne de la matrice séparés par un séparateur ! Veuillez le respecter !\n")
        G=Gfilling_forced2(k, n)                 #pour la matrice generatrice
        CODE=code(k,G)                           #generation de tous les mots du code dans une liste   
        
    #-----------------affichage des mots du code--------------------------------------------
    print("\nVoici la liste des mots du code ! ")
    print(np.array(CODE),"\n")
    
    #-----------------affichage matrice de controle---------------------------------------
    H=controle(G)
    print("la matrice de controle de votre code est :\n",np.array(H))
    
    message=Matrix(message)  
    if wordincode(message,H,k,n):
        print("Votre mot n'est pas erroné ! C'est bel et bien un mot valide !\nCependant lancons tout de même l'execution ! ")
        return(G,H,k,n,message,CODE,True)
    
    
    return (G,H,k,n,message,CODE,False)        #un tuple
