# -*- coding: utf-8 -*-
"""
************************
@author : Gabin
@contact : gabin.mondongou@auxlazaristeslasalle.fr
created on : Tue Apr 04 10:46:21 2023
last mod : 2023
title : notitle
goals : brief description
to do : what should be done next time
************************* """

""" ********************
    **** Imports ****
    ******************** """
# no data0

""" ********************
    **** Classes ****
    ******************** """
# no data

""" ********************
    **** Functions ****
    ******************** """

def condition_Dirac(matrice): # Verifie la condition de Dirac qui dit qu'un cylce hamiltonien peut exister seuleument si deg(sommet) >= n/2
    matrice_ligne_sans_zeros = [[el for el in ligne if el != 0] for ligne in matrice]
    for i in range(len(matrice)):
        if len(matrice_ligne_sans_zeros[i]) < (len(matrice)/2): # la matrice est symetrique donc len(matrice) correspond au nombre de sommets
            return False
    return True
        

   
""" ********************
    **** Global Var ****
    ******************** """
# no data

""" **************
    **** Main ****
    ************** """
# no data