# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:40:01 2022

@author: user
"""

from sympy import Matrix
import numpy as np
import random

def aleatorygenerateset(generatrix,k,n,s,Inset):  #generatrix est un objet de type matrix, Inset est une liste de liste
    
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
            #print(Iset)
            #a=input("pause:")
            if I in Iset:
                GI=list()                        #on retransforme GI en liste et on la vide pour pouvoir recommenecer
                print("a")
                #print(Iset)
                #a=input("pause :")
                continue
            else:
                Iset.append(I)                  #Si I n'a pas encore été selectionnée on l'ajoute dans Iset 
                GJ=[]
                GL=[]
                boolean=True                    #pour sortir de la boucle     
                def isIN(x):                     #va retourner les true si x n est pas dans I.
                   if(x in I)!=True:
                       return True
                
                R=list(filter(isIN,r))         #filter() va appeler isIn pour chaque element, le complementaire de I dans r
                l=0
                d=0
                J=[]
                L=[]
                print(R,"\n")
                for l in R:
                    L.append(l)
                    GL.append(np.array(generatrix)[:,l]) #ajout de s colonnes dans GL
                    d=d+1
                    if d==s:
                        break
                GL=Matrix(GL).T
                
                def isIN(x):                     #va retourner les true si x n est pas dans L.
                   if(x in L)!=True:
                       return True
                J=list(filter(isIN,R)) 
                for j in J:
                    GJ.append(np.array(generatrix)[:,j])
                GJ=Matrix(GJ).T
                print(I,"\n",L,"\n",J,"\n",Iset)         #POUR LE TEST
                
                print("\n",np.array(GL))  
                print("\n",np.array(GJ)) 
                return (GI,GL,GJ,I,L,J,Iset)             #GI ,GL, GJ de taille  k*k, k*s ,k*(n-k-s)  respectivement
        else:
            GI=[]

            
#-------------POUR STERN----------------------------------------------------------------------------------------------------------
def randomdivision(ZL,ZJ,k):                          #prend en entrée les matrices de taille k*s, k*(n-k-s) respectivement,m=n-k-s
    
    a=sorted(range(k))
    k=int(k/2)
    Z1L=[]
    Z2L=[]
    Z1J=[]
    Z2J=[]
    b=sorted(random.sample(a,k))
    def isIN(x):                     
       if(x in b)!=True:
           return True
    c=list(filter(isIN,a)) 
    print(a,b,c)
    
    for i in b:
        Z1L.append(np.array(ZL)[i,:])                   #ajout des colonnes dans GI
        Z1J.append(np.array(ZJ)[i,:])
    
    for i in c:
        Z2L.append(np.array(ZL)[i,:])                   #ajout des colonnes dans GI
        Z2J.append(np.array(ZJ)[i,:])
    Z1L=Matrix(Z1L)
    Z1J=Matrix(Z1J) 
    Z2L=Matrix(Z2L)
    Z2J=Matrix(Z2J) 
        
    print(np.array(Z1L),"\n",np.array(Z2L),"\n",np.array(Z1J),"\n",np.array(Z2J),"\n")

    return (Z1L,Z2L,Z1J,Z2J)
            
            
            
                                  