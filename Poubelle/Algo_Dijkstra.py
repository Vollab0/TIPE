# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Mon Jan 16 23:10:46 2023
last mod : 
title : 
goals : 
to do : 
************************* """

""" ********************
    **** Imports ****
    ******************** """
# no data
import numpy as np

""" ********************
    **** Classes ****
    ******************** """
# no data


""" ********************
    **** Functions ****
    ******************** """
    
def plus_court_chemin(matadj,start,end):
    assert type(start) == int , "L'indice de la station de départ doit être un entier"
    assert type(end) == int , "L'indice de la station d'arrivé doit être un entier"
    n = len(matadj)
    distance = [float('inf') for i in range(n)]
    precedent = [None for i in range(n)]
    visite = [False for i in range(n)]
    distance[start] = 0
    file = [start]
    
    while len(file)!=0 :
        sommet = file[0]
        visite[sommet] = True
        del file[0]
        for i in range(n):
            if matadj[sommet][i] != 0 and visite[i] == False:
                if distance[i] > distance[sommet] + matadj[sommet][i]:
                    distance[i] = distance[sommet] + matadj[sommet][i]
                    precedent[i] = sommet
                if i not in file:
                    file.append(i)
    
    chemin = [end]
    sommet = end
    
    while sommet != start:
        chemin.append(precedent[sommet])
        sommet=precedent[sommet]
    
    chemin.reverse()
        
    return chemin,distance[end]


""" ********************
    **** Global Var ****
    ******************** """
# no data


""" **************
    **** Main ****
    ************** """
# no data


mat=np.array([[0,1,2,0,0],
                    [0,0,0,3,0],
                    [0,0,0,1,0],
                    [0,0,0,0,3],
                    [0,2,1,0,0]])

print(plus_court_chemin(mat,0,4))









