# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:45:44 2022

LE BUT DE CETTE PARTIE EST DE DEFINIR LA FONCTION DE SELECTION DES ENSEMBLES D'INFORMATION' 

@author: user
"""
import random
from sympy import Matrix
import numpy as np

def aleatorygenerateset(generatrix,k,n,Inset):  #generatrix est un objet de type matrix, Inset est une liste de liste
    
    GI=[]                                       #liste qui sera transformée en matrix
    boolean=False
    Iset=[]                                     #ensemble des blocs d'informations
    I=[]                                        #ensemble d'informations
    
    if Inset!=[]:                               #si Inset n est pas vide alors je passe Inset à I
        Iset=Inset       
    r=sorted(range(n))                          #trie dans l ordre la liste sortie par range()
    #print(r,"\n")                              #pour test
    while boolean==False:
        I=sorted(random.sample(r,k))            #selection aléatoire de k elements parmi n sans repetitions
        print("\n",I)                 
        for i in I:
            GI.append(np.array(generatrix)[:,i])#ajout des colonnes dans GI
        GI=Matrix(GI).T                         #conversion pour les operations matricielles et transposition pour avoir dans la matrice de ligne k*k issue de celle de k*n.
       
        print(np.array(GI))                    #pour test     
        print("\n")                               
        if (GI.det()!=0):
            if I in Iset:
                GI=list()                        #on retransforme GI en liste et on la vide pour pouvoir recommenecer
                continue
            else:
                Iset.append(I)                  #Si I n'a pas encore été selectionnée on l'ajoute dans Iset 
                GJ=[]
                boolean=True                    #pour sortir de la boucle     
                def isIN(x):                     #va retourner les true si x n est pas dans I.
                   if(x in I)!=True:
                       return True
                J=list(filter(isIN,r))         #filter() va appeler isIn pour chaque element
                print(I,"\n",J,"\n",Iset)      #POUR LE TEST
                for j in J:
                    GJ.append(np.array(generatrix)[:,j]) #ajout des colonnes dans GJ
                GJ=Matrix(GJ).T
                print("\n",np.array(GJ))
                
                return (GI,GJ,I,J,Iset)        #GI ,GJ de taille  k*k, k*(n-k)  respectivement
        else:
            GI=list()
            
                                  
            
            
                
        
    
   