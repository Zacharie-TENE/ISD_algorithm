# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:19:21 2022
ALLEZ LE CODE S'EXECUTE ! '

@author: user
"""
import os
from complexityisd import efficiencyalgorithm
from informationset import leebrickellISD

val=leebrickellISD()

if val==0:
    print("\nPASSONS A LA PROCHAINE ETAPE ! ")
else:
    print("\nNavré que le mot ne puisse etre rectifé mais passons à la prochaine ETAPE")

efficiencyalgorithm()

      
"""
#tolist() permet de convertir un np.array() ou sympy.matrix() en une liste
#print(message)
#G=generatrice.Gautogeneration(k, n)
#G=generatrice.Gfilling_forced(G, k, n)print(G)"""
      
os.system("PAUSE")