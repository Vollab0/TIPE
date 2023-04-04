# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Tue Mar 21 10:11:17 2023
last mod : 
title : 
goals : 
to do : 
************************* """

""" ********************
    **** Imports ****
    ******************** """

import numpy as np
import heapq

""" ********************
    **** Classes ****
    ******************** """



""" ********************
    **** Functions ****
    ******************** """

def mat_to_dico(matrice):
    dico = {}
    for i in range(len(matrice)):
        dico[i] = {}
        for j in range(len(mat_graph[i])):
            if matrice[i][j] != 0:
                dico[i][j] = matrice[i][j]
    return dico

def dijkstra_dic(graph,depart,arrivee):
    
    distances = {sommet : float('inf') for sommet in graph}
    distances[depart] = 0
    heap = [(0, depart)]
    sommet_pre = {}
    
    while heap:
        (distance_act, sommet_act) = heapq.heappop(heap)
        
        if sommet_act == arrivee:
            chemin = []
            
            while sommet_act in sommet_pre:
                chemin.insert(0, sommet_act)
                sommet_act = sommet_pre[sommet_act]
            
            chemin.insert(0, depart)
            return (chemin, distance_act)
        
        for voisins, distance in graph[sommet_act].items():
            distance_temp = distances[sommet_act] + distance
            
            if distance_temp < distances[voisins]:
                distances[voisins] = distance_temp
                sommet_pre[voisins] = sommet_act
                heapq.heappush(heap, (distance_temp, voisins))
                
    return None

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

dic_graph = mat_to_dico(mat_graph)

print(dijkstra_dic(dic_graph,1,4))


