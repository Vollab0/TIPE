# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Mon Feb 13 19:18:32 2023
last mod : 
title : 
goals : 
to do : 
************************* """

""" ********************
    **** Imports ****
    ******************** """

import numpy as np

""" ********************
    **** Classes ****
    ******************** """
# no data


""" ********************
    **** Functions ****
    ******************** """

def voisins(matrice,sommet):
    liste_voisins=[i for i in range(len(matrice)) if matrice[sommet][i]!=0]
    return liste_voisins

def centralite(graph):
    sommets_principaux={}
    n=len(graph)
    for i in range(n):
        if len(voisins(graph,i))>2:
            sommets_principaux[i]=len(voisins(graph,i))
    return sommets_principaux


    


""" ********************
    **** Global Var ****
    ******************** """
# no data


""" **************
    **** Main ****
    ************** """
# no data


mat_graph=np.array([[0,1,2,0,0],
                    [0,0,0,3,0],
                    [0,0,0,1,0],
                    [0,0,0,0,3],
                    [0,2,1,4,0]])


print(voisins(mat_graph,4))
print(centralite(mat_graph))

