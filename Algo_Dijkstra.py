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



""" ********************
    **** Global Var ****
    ******************** """



""" **************
    **** Main ****
    ************** """

matrice=np.array([[0,5,6,0],
                 [0,0,2,4],
                 [0,6,0,1],
                 [4,0,0,0]])


def pcc(matadj,start,end):
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
        
    return "le chemin le plus court pour aller de",start,"à",end,"est",chemin,"et il fait",distance[end],"km"

print(pcc(matrice,1,0))

"""

function shortestPath(adjMatrix, start, end)
    initialize variables
    while queue is not empty
        get current node from queue
        mark it as visited
        check all adjacent nodes
        update distance if a shorter path is found
        if not visited, add to queue
    construct path from previous nodes
    return path

"""











