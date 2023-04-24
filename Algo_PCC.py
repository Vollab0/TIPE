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
    assert type(start) == int , "L'indice de la station de départ doit être un entier"
    assert type(end) == int , "L'indice de la station d'arrivé doit être un entier"
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
        sommet_act = sommet_pre[sommet_act]
    
    chemin.reverse()
        
    return chemin, distances[end]

##########

def mat_to_dico(matrice):
    dico = {}
    for i in range(len(matrice)):
        dico[i] = {}
        for j in range(len(matrice[i])):
            if matrice[i][j] != 0:
                dico[i][j] = matrice[i][j]
    return dico

##########

def dijkstra_dic(graphe,depart,arrivee):
    dico=mat_to_dico(graphe)
    distances = {sommet : float('inf') for sommet in dico}
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
        
        for voisins, distance in dico[sommet_act].items():
            distance_temp = distances[sommet_act] + distance
            
            if distance_temp < distances[voisins]:
                distances[voisins] = distance_temp
                sommet_pre[voisins] = sommet_act
                heapq.heappush(heap, (distance_temp, voisins))
                
    return None

##########

def voisins(matrice,sommet):
    liste_voisins=[i for i in range(len(matrice)) if matrice[sommet][i]!=0]
    return liste_voisins

##########

def Astar(matrice,debut,fin):
    openlist=[debut]
    closedlist=[]
    parents={}
    poids={debut:0}
    heuristique={0:9, 1:5, 2:6, 3:4, 4:0}
    
    while len(openlist)!=0:
   
        cout = float("inf")
        for noeud in openlist:
            if poids[noeud]+heuristique[noeud]<cout:
                cout=poids[noeud]+heuristique[noeud]
                noeud_act=noeud
            
        if noeud_act == fin:
            chemin=[fin]
            dernier = fin
            while dernier != debut:
                chemin.append(parents[dernier])
                dernier = parents[dernier]
            return chemin[::-1]

        closedlist.append(noeud_act)
        openlist.remove(noeud_act)
                
        for voi in voisins(matrice,noeud_act):
            if voi not in closedlist:
                new_poids = poids[noeud_act] + matrice[noeud][voi]
            if voi not in openlist or new_poids < poids[voi]:
                parents[voi] = noeud_act
                poids[voi] = new_poids
                if voi not in openlist:
                    openlist.append(voi)
    
    return 'Nope'

""" ********************
    **** Global Var ****
    ******************** """



""" **************
    **** Main ****
    ************** """
