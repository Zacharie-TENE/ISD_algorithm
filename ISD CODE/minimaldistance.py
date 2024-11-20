# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:11:08 2022

DANS CE MODULE,NOUS AVONS REUNI TOUT CE QUI EST LIE DE PRET 
OU DE LOIN AUX NOTIONS DE DISTANCES ET POIDS MINIMAUX QUI SERA UTILISE DANS LA SUITE DE NOTRE PROGRAMME

@author: user
"""

from generationcode import vecMod2,uplets
from sympy import Matrix

#-----------distance minimale------------------------------------------------------------------------
def dmin(code, n, m):   #code est une liste ici, n=2^k, m=n(saisie par l'utilisateur).

    p = []

    for i in range(n-1):
        for j in range(i + 1, n):
            s= 0
            for k in range(m):
                if (code[i][k] != code[j][k]):
                    s = s + 1
            p.append(s)
    #print(min(p))
    return min(p)
  
#--------------fonction de calcul du poids de l'erreur--------------------------------------------------
def werror(eI,k):                  #pend en entrée un vecteur ligne e de taille 1*k
  s=0
  for i in range(k): 
        if (eI[0,i] != 0):
            s=s+1
  return s                         #retourne le poids de eI
  

#---------------calcul du poids de l'entité xj+(xi+ei)Z------------------------------------------------
def weightx(MI,MJ,eI,Z,k,n):       #tous les parametres vectoriels sont des vecteurs lignes
    s=0
    Entity=MJ-MI*Z-eI*Z            #vecteur de taille 1*(n-k)
    Entity=vecMod2(Entity.T)       #vecteur colonne modulo 2   
    Entity=Entity.transpose()      #vecteur Entity de depart mod 2
    for i in range(n-k): 
        if Entity[0,i]!=0:
            s=s+1
    return s                       #poids de Entity

#----------redefinition-------------------------------------------------------------------------------
def dmin2(code, n, m):             #code est une matrix ici, n=2^k, m=n.
    p = []

    for i in range(n-1):
        for j in range(i + 1, n):
            s= 0
            for k in range(m):
                if (code[i,k] != code[j,k]):
                    s = s + 1
            p.append(s)
    return min(p)


#--------generer toutes les erreurs de longueur et de poids <=p------------------------------------------
def eIgenerator(p,k): 
    eIsetp=[]
    eIset=uplets(k)                 #ne pas oublier que chaque element est une liste
    for i in eIset:
        s=werror(Matrix([i]),k)     ##attention aux paramètres: Matrix([i]) permet de convertir la liste i en vecteur ligne
        if(s<p+1):
            eIsetp.append(i)
    return eIsetp                   #retourne une liste des eI(sous forme de liste) de poids au plus p

#------------------------------------------------------------------------------------------------------
def packingradius(dmin):
    return int((dmin-1)/2)

def maxcapacityofcorrection(dmin):      #pas utile mais bon pourquoi pas?
    return int((dmin-1)/2)

def maxcapacityofdetection(dmin):
    return dmin-1

def verifyMDS(dmin,k,n):
    if dmin==n-k+1:
        return True                        #cas idéal
    else:
        return False
    
#-------------------------------------------------------------------------------------------------------------
def possible(codey,n,m,t):
     q=dmin(codey,n,m)
     if q>t:
         return False
     else:
         return True
    
#--------------pour STERN----GENERE LES VECTEUR EI DE POIDS P-----------------------------------------------------
def eIgeneratorSTERN(p,k): 
    eIsetp=[]
    eIset=uplets(k)                 #ne pas oublier que chaque element est une liste
    for i in eIset:
        s=werror(Matrix([i]),k)     ##attention aux paramètres: Matrix([i]) permet de convertir la liste i en vecteur ligne
        if s==p:
            eIsetp.append(i)
    return eIsetp       