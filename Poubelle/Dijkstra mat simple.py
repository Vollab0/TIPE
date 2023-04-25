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

import numpy as np

""" ********************
    **** Classes ****
    ******************** """



""" ********************
    **** Functions ****
    ******************** """

def dijkstra_mat(matadj,start,end):
    n = len(matadj)
    distances = [float('inf') for i in range(n)]
    sommet_pre = [None for i in range(n)]
    visite = [False for i in range(n)]
    distances[start] = 0
    file = [start]
    
    while len(file)!=0 :
        sommet_act = file[0]
        visite[sommet_act] = True
        del file[0]
        for i in range(n):
            if matadj[sommet_act][i] != 0 and visite[i] == False:
                if distances[i] > distances[sommet_act] + matadj[sommet_act][i]:
                    distances[i] = distances[sommet_act] + matadj[sommet_act][i]
                    sommet_pre[i] = sommet_act
                if i not in file:
                    file.append(i)
    
    chemin = [end]
    sommet_act = end
    
    while sommet_act != start:
        chemin.append(sommet_pre[sommet_act])
        sommet_act=sommet_pre[sommet_act]
    
    chemin.reverse()
        
    return chemin, distances[end]

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

print(dijkstra_mat(mat_graph,1,4))

    










