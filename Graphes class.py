# -*- coding: utf-8 -*-
"""
************************
@author : damie
@contact : damien.reynier@auxlazaristeslasalle.fr
created on : Tue Oct 18 10:37:38 2022
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

class graphe:
    def __init__(self,*args):
        self.edges = [ e for e in args ]
        self.nodes = []
        for e in self.edges:
            if e[0] not in self.nodes:
                self.nodes += [ e[0] ]
            if e[1] not in self.nodes:
                self.nodes += [ e[1] ]
                
    def mat(self):
        self.mat = np.zeros((len(self.nodes),len(self.nodes))) 
        for i in self.edges:
            self.mat[ self.nodes.index(i[0]) ][ self.nodes.index(i[1]) ] = i[2]
        return self.mat
    


""" ********************
    **** Functions ****
    ******************** """

def matrice_adj(a_s):
    """
    Créer un matrice d'adjacence
    a_s = nombre de sommets
    """
    return np.zeros((a_s,a_s))

""" ********************
    **** Global Var ****
    ******************** """



""" **************
    **** Main ****
    ************** """

G = graphe( ('A','D','1') , ('A','C','5') , ('B','C','7') , ('B','E','3') , ('B','B','2') , ('F','A','6'))
print( 'Les sommets de G sont : ', G.nodes )
print( 'Les arêtes pondérées de G sont :', G.edges )
print( 'La matrice d\'adjacence de G est :\n', G.mat() )