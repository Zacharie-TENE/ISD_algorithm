# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:09:49 2022

@author: user
"""
"""
DANS CE MDOULE SE TROUVE LES FONCTIONS PERMETTANT LE REMPLISSAGE DE LA MATRICE GENERATRICE
"""

import numpy as np 
from generationcode import matMod2
import sympy

#creation d'une matrice de taille k*n
def matrice(k,n): 
    return sympy.Matrix([[0 for j in range(0,n)] for i in range(0,k)])  
  
"""
#generatrix=matrice(k,n) , generatrion aléatoire, va servir?
def Gautogeneration(k,n):
    generatrix=np.random.randint(2,size=(k,n))
    return generatrix

L'utilisateur peut egalemet entrer les lignes de la matrice avec separateur ou pas.
remplissage de la matrice generatrice par l'utilisateur.Utilisé dans Gfilling_forced( )"""

def Gfilling(generatrix,k,n,symbol):                    #generatrix est de type matrix
    print("RAPPEL : Notre corps de base est {0,1} donc les opérations sont modulos 2 ! Merci! ")
    for i in range(k):
        var_bool=True
        while var_bool:
            ligne=input("Entrez les elements de la {}(ère)ieme ligne de la matrice separés par le caractère {} ( les entres en binaire) svp : ".format(i+1,symbol))
            ligne=ligne.split(symbol)
            var_bool=False
            for j in range(n):                          #si l'utilisateur entre un nombre de bits superieure, le surpus ne sera pas géré.aussi simple que ca
                try:
                    ligne[j]=int(ligne[j])
                    generatrix[i,j]=ligne[j] 
                except:
                    print("\nEntrée invalide ! ")
                    print("Veuillez recommencer svp")
                    var_bool=True
                    break
    generatrix=matMod2(generatrix,k)                   #la matrice mod 2
    return generatrix                                  #retourne un objet de type matrix
                
#forcer l'utilisateur à entrer une matrice dont les vecteurs lignes sont linéairement indépendants
#si un cas ne marche pas on retire le tant que?
def Gfilling_forced(k,n,symbol):
    generatrix=matrice(k, n)                           #genere la matrice
    print("Début de la saisie des coefficients de la matrice génératrice de votre code : ")
    test=True
    while test:
        generatrix=Gfilling(generatrix,k,n,symbol)
        test=False
        if generatrix.rank()!=k:
            print("Les vecteurs lignes entrés ne sont pas linéairement indépedants : Veuillez recommencer svp !")
            #generatrix=np.array(generatrix)           #reconversion en np.array() pour l'appel de la fonction Gfilling()
            test=True
        if test==False:
            print("Voici la matrice génératrice que vous avez entrée :\n", np.array(generatrix))
            reponse_user=input("Voulez-vous la modifier ? entrer OUI/YES sinon saisissez NON/NO : ")
            if reponse_user in ["yes","oui","YES","OUI","O","o","y","Y"]:
                test=True                             #allez,on recommence 
                print("\nRESTART")
            else:
                test=False
                return generatrix                     #retourne un objet de type matrix   
                
#------------------------------------------------------------------------------------------------------------       
"""juste des redefinitions de fonctions si l'utilisateur préfère entrer les coef sans séparateur."""

def Gfilling2(generatrix,k,n):                   
    print("RAPPEL : Notre corps de base est {0,1} donc les opérations sont modulos 2 ! Merci! ")
    for i in range(k):
        var_bool=True
        while var_bool:
            ligne=list(input("Entrez les elements de la {}(ère)ieme ligne (les entres en binaire) svp : ".format(i+1)))
            var_bool=False
            for j in range(n):
                try:
                    ligne[j]=int(ligne[j])  #si l'utilisateur entre des lignes de plus de n valeurs à recuperer ,le reste sera ignoré
                    generatrix[i,j]=ligne[j] 
                except:
                    print("\nEntrée invalide ! ")
                    print("Veuillez recommencer svp")
                    var_bool=True
                    break
    generatrix=matMod2(generatrix,k)
    return generatrix                                  #retourne un objet de type matrix                       
                

def Gfilling_forced2(k,n):
    generatrix=matrice(k, n)                    
    print("Début de la saisie des coefficients de la matrice génératrice de votre code : ")
    test=True
    while test:
        generatrix=Gfilling2(generatrix,k,n)
        test=False
        if generatrix.rank()!=k:
            print("Les vecteurs lignes entrés ne sont pas linéairement indépedants : Veuillez recommencer svp !")
            test=True
        if test==False:
            print("Voici la matrice génératrice que vous avez entrée :\n", np.array(generatrix))
            reponse_user=input("Voulez-vous la modifier ? entrer OUI/YES sinon saisissez NON/NO : ")
            if reponse_user in ["yes","oui","YES","OUI","O","o","y","Y"]:
                test=True
                print("\nRESTART")
            else:
                test=False
                return generatrix  
   