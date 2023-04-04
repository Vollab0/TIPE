# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Tue Apr  4 10:26:27 2023
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



""" ********************
    **** Functions ****
    ******************** """

def voisins(matrice,sommet):
    liste_voisins=[i for i in range(len(matrice)) if matrice[sommet][i]!=0]
    return liste_voisins



def Astar(matrice,debut,fin):
    openlist=[debut]
    closedlist=[]
    h_cout={debut:0}
    f_cout={0:9, 1:5, 2:6, 3:4, 4:0}
    
    while len(openlist)!=0:

        for i in range(len(openlist)):
            cout=float('inf')
            if h_cout[i]+f_cout[i]<cout:
                cout=h_cout[i]+f_cout[i]
                noeud_act=i
            if i == fin:
                return 'Cool'
            
                
            for j in range(len(voisins(matrice,i))):
                h_cout[j]=matrice[i][j]







""" ********************
    **** Global Var ****
    ******************** """



""" **************
    **** Main ****
    ************** """

mat_graph=np.array([[0,1,0,0,0],
                    [0,0,0,3,0],
                    [2,0,0,1,0],
                    [3,1,0,0,3],
                    [0,2,1,0,0]])


print(voisins(mat_graph,2))

