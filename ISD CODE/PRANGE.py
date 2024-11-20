# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:41:21 2022

ALGORITHME DE PRANGE

@author: user
"""
from presentation import presentation
from aleatorygenerate import aleatorygenerateset
from minimaldistance import dmin,packingradius,maxcapacityofdetection,verifyMDS,possible,werror
from generationcode import matMod2,vecMod2,wordincode
from sympy import Matrix
import numpy as np

def createIJ(M,I,J): #ICI M est un objet matrix de taille 1*n :vecteur sympy(colonnes),I,J des listes
    MI=[]
    MJ=[]
    for i in I:
        MI.append(M[i]) 
    for j in J:
        MJ.append(M[j])
    MJ=Matrix(MJ).T
    MI=Matrix(MI).T
    
    return MI,MJ                                     #retourne des vecteurs de taille 1*k, 1*(n-k) respectivement

def Zfixing(U,GJ,k):
    return matMod2(U*GJ,k) #matrice de taille k*n

def efixing(mJ,mI,Z):                            #LES PARAMETRES VECTORIELS SONT DES VECTEURS LIGNES
    eJ=mJ-mI*Z
    eJ=eJ.transpose()
    eJ=vecMod2(eJ)
    eJ=vecMod2(eJ).transpose()
    print(np.array(eJ))
    return eJ                                        #retourne eJ

def rearrange(MI,MJ):                                #DES VECTEURS LIGNES EN ENTREE ! imperatif !
    M=[]
    M.extend(MI)
    M.extend(MJ)
    M=Matrix(M).transpose()
    return M                                         #vecteur ligne M=(MI|MJ)

def prangeISD(): 
    (G,H,k,n,message,Code,value)=presentation()   #on a G,H,message de type matrix et I,J ,Code des listes , value booleen
    message=message.T                             #desormais vecteur ligne
    print("\nRappelons que le message entré est : ",np.array(message))
    d=dmin(Code,pow(2,k),n)
    Inset=[] 
    sortie=0
    t=packingradius(d)
    mcc=maxcapacityofdetection(d)
    Code.extend(message.tolist())   
    print("\nAprès analyse des paramètres entrés :")
    print("La capacité maximale de détection d'erreur de votre code est de : ",mcc)
    print("La capacité maximale de correction d'erreur de votre code est de : ",t)
    print("La distance minimale de HAMMING de votre code est de : ",d)
    print("Le poids minimal de Hamming de votre code est de : ",d) #dmin=wmin
    if verifyMDS(d, k, n):
        print("Votre code est un MDS ! ")
    else:
        print("Votre code n'est pas un MDS ! ")
    if possible(Code,pow(2,k)+1,n,t):
        print("Le mot entré peut être décodé ! Nous allons donc poursuive ! \n")
    else:
        print("Trop d'erreus .Nous sommes désolés ! Le mot entré ne peut être décodé ! ")
        print("ARRET DU PROGRAMME ! ")
        return -1
    if value:
        print("Le mot saisi n'est pas un un mot du code ! ")
        #syn=syndrome(message, H)  
        #print(np.array(error))     
    print("\nExecution de l'algorithme de PRANGE\n")
    q=n-k                               #nbre de colonne que doit avoir eJ
    Trouve=False
    while Trouve==False:     
        index=0                        #pour verifier si la boucle va se reexecuter           
        (GI,GJ,I,J,Inset)=aleatorygenerateset(G,k,n,Inset)
        U=GI**-1
        Z=Zfixing(U,GJ,k)
        print("\n",np.array(Z))
        (mI,mJ)=createIJ(message, I, J)
        print("\n",np.array(mI),"\n",np.array(mJ),"\n")
      
        eJ=efixing(mJ, mI, Z)
        w=werror(eJ,q)
        if w<t+1:
            eI=Matrix([[0]*k])
            e=rearrange(eI, eJ)
            first_word=vecMod2(mI*U).transpose()
            Trouve=True
            print("\nle mot de départ ( décodé ) avant le bruit est : ",np.array(first_word))
            print("Le mot obtenu (codé ) après encodage sans l'erreur était : ", np.array(vecMod2(first_word*G ).T))
            print("L'erreur infilté était le vecteur ( en considérant (mI,mJ) ) : ",np.array(e))
            print("L'erreur ajoutée directement suite à l'encodage était : ",np.array(vecMod2(message-first_word*G ).T))
            index=1
        if index==0:                #S'execute slmnt si l'iteration recommence
            print("On recommence ! le nombre d'essaie maximal n'a pas encore été atteint ! \n")
        sortie=sortie+1
        if sortie==250:
            print("\nLa boucle de notre algorithme s'est déjà éxecutée 250 fois sans trouver ! ")
            print("Il semblerait donc que le décodage prendra trop de temps ! Donc Le programme s'est arrêté ! Merci pour votre compréhension ")
            break
    if wordincode((first_word*G).transpose(),H,k,n):
        print("\nLE MOT DECODE OBTENU EST BIEN l'ANTECEDANT D'UN MOT DU CODE ! ")
    return 0

