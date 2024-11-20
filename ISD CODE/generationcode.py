# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:10:12 2022

DANS CE MODULE SE TROUVE TOUTES LES FONCTIONS DE BASE

@author: user
"""

#F={0,1}
from  sympy import Matrix
from sympy import init_printing

#from numpy import*
#import numpy as np
#import numpy.linalg as alg
#from sympy import*

init_printing(use_unicode=True) 
#use_unicode=True est facultatif   
#pour l'affichage des caracteres unicodes pour les expressions mathématiques.
#matrice identité c'est Identity(n) ou eye(n)


#pour engendrer tous les mots binaires de longueur k (longueur du mot de {0,1}^k)
def uplets(k):
    from itertools import product
    K=[range(0,2)]*k
    Fn=(Matrix(list(product(*K)))).tolist() #product() retourne un tuple.
    return Fn

#pour avoir tous les mots du code
#Matrice.shape() retourne la taille d une matrice dans un (tuple) modifiable lors d'une affectation multiple
def code(k,generatrix):
    Fn=uplets(k)
    Code=[]
    for i in Fn:
        Code.append(listMod2(list(Matrix(k,1,i).T*generatrix)))
        """"Code sera une liste de listes.
            Une liste d element est vu comme un vecteur colone par Matrix(list) 
            raison pour laquelle on transpose pour avoir un vecteur ligne."""
    return Code
    """le nbre de ligne vaut 2^k et celui des colonnes n. Chaque ligne constitue un mot du code
        print(list(Matrix(k,1,i).Transpose*generatrix) ) pour le test"""
        
#pour convertir les elts d'une liste mod 2              
def listMod2 (liste):
    return [i%2 for i in liste]

#pour convertir un vecteur sympy colonne n*1 mod 2
def vecMod2(vector):                     
    return Matrix (listMod2(vector))     #retourne un vecteur colonne

"""une redefinition de la fonction précédente pour un vecteur sympy de taille 1*n
def vecMod2x(vector,n):                 
    vect=[]
    for i in range(n): 
        vect.apend(vector[0,i]%2)
    return Matrix(vect) """  

"""fonction qui pour une liste de liste retourne une structure de même type (mod2).On en aura peut etre besoin ? """ 
def llistMod2 (listoflist):
    r=[]
    #n=len(liste)
    for i in listoflist:
        r.append(listMod2(i))
    return r

#de meme pour une matrice
def matMod2(matrice,k):       #prend en entrée une matrice de type matrix de taille k*n
    r=[]    
    for i in range(k):
        r.append(listMod2(matrice[i,:]))
    return Matrix(r)

#determination de la matrice de controle H,generatrix.nullspace() retourne une liste.
def controle(generatrix):
    return Matrix(llistMod2(generatrix.nullspace())) 
    #calcule le noyau de generatrix et convertie la liste en matrice.
    #taille de sortie (n-k)*n

    """paritix=np.random.randint(2,size=(n,n-k))
    for i in uplets(n):
        if vecMod2(generatrix*Matrix(i))==Matrix([0]*k):
            paritix.append(i)
            return Matrix(paritix[1])
            autre facon de trouver la matrice de controle"""

#fonction qui calcule le syndrome d'un mot recu , necessaire?
def syndrome(message,H):                      #message est un vecteur sympy de taille 1*n donc vecteur ligne
    message=message.T                         #pour mettre en colonne
    return vecMod2(H*message).transpose()     #retourne un vecteur sympy en ligne 1*k

"""fonction qui va nous retourner le e vecteur unité (de dimension n) et qui va nous
permettre de trouver les syndromes (i.e. de trouver les erreurs), utile?"""
def unitVector(n,i):
    return Matrix([1 if j==i else 0 for j in range(n)])     #retourne un vecteur sympy de taille n*1

"""
fonction qui verifiera si le mot obtenu est un mot du code
mot ici, est un vecteur colonne sympy de taille n*1
"""
def wordincode(mot,H,k,n): 
    if  matMod2(H*mot,n-k)==Matrix([0]*(n-k)):
        #print("lE MOT ENTRE EST UN MOT DU CODE ! ")
        return True
    else:
        #print("Merci ! Ce mot est bien un mot corrompu ! ")
        return False

#--------------------------------------------------------------------------------------------

     