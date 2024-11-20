# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 06:41:10 2022

PROJET: ISD

@author: user
"""
import os
from complexityisd import efficiencyalgorithm
from informationset import leebrickellISD
from LEON import leonISD
from PRANGE import prangeISD
from STERN import sternISD

print("NOS SALUTATIONS ! NOUS ESPERONS QUE VOUS VOUS PORTEZ BIEN ! ")
print("Pour cette partie, nous vous proposons de tester 02 algorithmes !\n ")
print("1  : LEE-BRICKELL ")
print("2  : PRANGE ")
print("3  : LEON ")
print("4  : STERN ")

valide=True
while valide==True:
    reponse=input("\nQUEL ALGORITHME SOUHAITEZ-VOUS EXECUTER ?(utiliser les numeros svp ) :  ")
    try:
        reponse=int(reponse)
        if reponse>0 and reponse<5:
            valide=False
    except:
        print("Entrée invalide ! veuillez recommencer ! ")
if reponse==1:
    val=leebrickellISD()

    if val==0:
        print("\nPASSONS A LA PROCHAINE ETAPE ! ")
    else:
        print("\nNavré que le mot ne puisse etre rectifé mais passons à la prochaine ETAPE")
    efficiencyalgorithm()
elif reponse==2:
    val=prangeISD()

    if val==0:
        print("\nPASSONS A LA PROCHAINE ETAPE ! ")
    else:
        print("\nNavré que le mot ne puisse etre rectifé mais passons à la prochaine ETAPE")

    efficiencyalgorithm()
    

elif reponse==3:
    val=leonISD()

    if val==0:
        print("\nPASSONS A LA PROCHAINE ETAPE ! ")
    else:
        print("\nNavré que le mot ne puisse etre rectifé mais passons à la prochaine ETAPE")

    efficiencyalgorithm()
     
else:
    val=sternISD()

    if val==0:
        print("\nPASSONS A LA PROCHAINE ETAPE ! ")
    else:
        print("\nNavré que le mot ne puisse etre rectifé mais passons à la prochaine ETAPE")

    efficiencyalgorithm()    
    
    
os.system("PAUSE")