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

mat_graph=np.array([[0,1,2,0,0],
                    [0,0,0,3,0],
                    [0,0,0,1,0],
                    [0,0,0,0,3],
                    [0,2,1,0,0]])


"""print(voisins(mat_graph,2))"""
print(Astar(mat_graph,4,3))
