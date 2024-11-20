# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:39:26 2022
ALGORITHME DE LEON

@author: user
"""

from presentation import presentation
from util import aleatorygenerateset
from minimaldistance import dmin,eIgenerator,packingradius,maxcapacityofdetection,verifyMDS,werror,possible
from generationcode import matMod2,vecMod2,wordincode
from sympy import Matrix
import numpy as np

def createIJ(M,I,L,J):                              #ICI M est un objet matrix de taille 1*n :vecteur sympy(colonnes),I,L,J des listes
    MI=[]
    ML=[]
    MJ=[]
    for i in I:
        MI.append(M[i]) 
    for l in L:
        ML.append(M[l])
    for j in J:
        MJ.append(M[j])
    ML=Matrix(ML).T
    MJ=Matrix(MJ).T
    MI=Matrix(MI).T
    
    return MI,ML,MJ                                 #retourne des vecteurs de taille 1*k, 1*s ,1*(n-k-s) respectivement

def Zfixing(U,GM,k):
    return matMod2(U*GM,k)                          #matrice de taille k*m ,m nbre de colonnes de la matrice GM

def efixing(m1,mI,eI,Z):                             #LES PARAMETRES VECTORIELS SONT DES VECTEURS LIGNES
    e1=m1-mI*Z-eI*Z
    e1=e1.transpose()
    e1=vecMod2(e1)
    e1=vecMod2(e1).transpose()
    print(np.array(e1))
    return e1
    
def rearrange(MI,ML,MJ):                            #DES VECTEURS LIGNES EN ENTREE ! imperatif !
    M=[]
    M.extend(MI)
    M.extend(ML)
    M.extend(MJ)
    M=Matrix(M).transpose()
    return M                                       #vecteur ligne M=(MI|MJ)

#on va reussir , p est un paramètre fixé à l'avance, p vaut 2
def leonISD(): 
    (G,H,k,n,message,Code,value)=presentation()   #on a G,H,message de type matrix et I,J ,Code des listes , value booleen
    #p,s=2,2                                      #valeurs par défaut
    
    bon=True
    while bon==True:                              #laisser le choix à l'utilisateur d'entrer les valeusr de p et s sous contrainte 
        s=input("\nVeuillez entrer le nombre de positions de redondance de S : s < {} :".format(n-k))  
        p=input("Veuillez entrer la valeur du poids de l'erreur autorisée sur l'ensemble des positions ( paramètre p < {}) : ".format(k+int(s)))
        try:
            p=int(p)
            s=int(s)
            if p<k+s and p>=0 and s<n-k and s>=0:
                bon=False
            else:
                print("Les valeurs de p et s entrées ne sont pas autorisées ou compatibles ! Veuillez recommencer .")
        except:
            print("les valeurs entrées ne sont pas valides ! VEUILLEZ REPRENDRE ! ")
    
    
    eIsetp=eIgenerator(p,k)
    message=message.T                          #desormais vecteur ligne
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
    print("\nExecution de l'algorithme de LEON\n")
    Trouve=False
    while Trouve==False:     
        index=0                                   
        (GI,GL,GJ,I,L,J,Inset)=aleatorygenerateset(G,k,n,s,Inset)
        U=GI**-1
        ZL=Zfixing(U,GL,k)
        ZJ=Zfixing(U,GJ,k)
        print("\n",np.array(ZL))
        print("\n",np.array(ZJ))
        (mI,mL,mJ)=createIJ(message, I,L,J)
        print("\n",np.array(mI),"\n",np.array(mL),"\n",np.array(mJ),"\n")
        for eI in eIsetp:
            eI=Matrix([eI])
            weI=werror(eI, k)
            if weI <p+1:
                eL=efixing(mL, mI,eI, ZL)
                wL=werror(eL,s)
                if wL<p-weI+1:
                    eJ=efixing(mJ,mI,eI,ZJ)
                    wJ=werror(eJ,n-k-s)
                    if wJ<t-wL-weI+1:
                        e=rearrange(eI,eL,eJ)
                        first_word=vecMod2(mI*U-eI*U).transpose()
                        Trouve=True
                        print("\nle mot de départ ( décodé ) avant le bruit est : ",np.array(first_word))
                        print("Le mot obtenu (codé ) après encodage sans l'erreur était : ", np.array(vecMod2(first_word*G ).T))
                        print("L'erreur infiltrée était le vecteur ( en considérant (mI,mL,mJ) ) : ",np.array(e))
                        print("L'erreur ajoutée directement suite à l'encodage était : ",np.array(vecMod2(message-first_word*G ).T))
                        if wordincode((first_word*G).transpose(),H,k,n):
                            print("\nLE MOT DECODE OBTENU EST BIEN l'ANTECEDANT D'UN MOT DU CODE ! \n")
                        return 0
                        
        if index==0:
            print("On recommence ! le nombre d'essaie maximal n'a pas encore été atteint ! \n")
        sortie=sortie+1
        if sortie==250:
            print("\nLa boucle de notre algorithme s'est déjà éxecutée 250 fois sans trouver ! ")
            print("Il semblerait que le décodage prendra trop de temps ! Donc Le programme va s'arrêter ! Merci pour votre compréhension ")
            return 0
    
   
        
        
        