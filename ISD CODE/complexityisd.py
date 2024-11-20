# -*- coding: utf-8 -*-
#from math import*

"""
Created on Mon Nov 14 12:11:08 2022

DANS CE MODULE SE TROUVE LA PARTIE LIEE AUX COMPLEXITES DE QUELQUES ALGORITHMES DE L'ISD
CETTE ÉTUDE NE CONCERNE QUE LES ALGORITHMES DE PRANGE, LEE-BRICKELL ET LEON

@author: user
"""
import math

def complex_Prange(n,k,t):
    if k > n-t:
        print("Votre complexité est de l'ordre de : ", n*n)
    else:
        return (math.comb(n,k)*(n*k*k + n*k + 2*n -k*k -2*k))/(2*math.comb(n-t,k))
def complex_lee(n,k,t):     #la valeur de p a été fixé a 2
    if k > n:
        print("Votre complexité est de l'ordre de : ", n*n)
    else:
        x=(math.comb(n-t,k)+t*math.comb(n-t,k-1)+t*(t-1)*math.comb(n-t,k-2)/2)/math.comb(n,k)
        return (7*n*k*k-6*k*k*k+4*n*k-2*k*k+2*n-2*k)/(4*x)
def complex_leon(n,k,t):    # les valeurs de p et a ont ete fixé à 2 et 2 respectivement, t=packing radius
    if k > n:
        print("Votre complexité est de l'ordre de : ", n*n)
    else:
        x=(math.comb(n-t,k+2) +t*math.comb(n-t,k+1)+t*(t-1)*math.comb(n-t,k)/2)/math.comb(n,k+2)
        return (2*n*k*k-3*k*k*k+n*k-k*k+n-k)/(4*x)

def efficiencyalgorithm():
    print("\nBien que nous avons implémenté l'algorithme de LEE-BRICKELl , nous vous proposons de connaitre l'algorithme ISD de notre base de donnée le plus efficace en fonction des paramètres d'entrés ! ")
    
    n=int(input("Entrer la longueur du code (n) : "))
    k=int(input("Entrer la dimension du code (k) : "))
    t=int(input("Entrer le rayon de recouvrement de votre code (t) : "))
    F=[complex_leon(n,k,t), complex_lee(n,k,t),complex_Prange(n,k,t)]
    b=min(F)
    if b==complex_Prange(n,k,t):
        print("L'algorithme le plus éfficace pour votre problème est celui de Prange avec : ",complex_Prange(n,k,t),"opérations élémentaires et son logarithme en base 2 est ",math.log(complex_Prange(n,k,t),2))
    elif b==complex_lee(n,k,t):
        print("L'algorithme le plus éfficace pour votre problème est celui de lee avec : ",complex_lee(n,k,t),"opérations élémentaires et son logarithme  en base 2 est ",math.log(complex_lee(n,k,t),2))
    else:
         print("L'algorithme le plus éfficace pour votre problème est celui de leon avec : ",complex_leon(n,k,t),"opÃ©rations élémentaires et son logarithme en base 2 est ",math.log(complex_leon(n,k,t),2))
