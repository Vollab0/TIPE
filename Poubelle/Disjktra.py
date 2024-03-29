# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Thu Mar 23 23:12:38 2023
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


print(dijkstra_mat(mat_graph,1,4),"mat")
print(dijkstra_dic(dic_graph,1,4),"dico")