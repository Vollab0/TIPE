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
    
def densite(graph):
    n=len(graph)
    somme_aretes=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0:
                somme_aretes+=1
    return somme_aretes/(n*(n-1)/2)
    


""" ********************
    **** Global Var ****
    ******************** """
# no data


""" **************
    **** Main ****
    ************** """
# no data


