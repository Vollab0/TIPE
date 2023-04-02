# -*- coding: utf-8 -*-
"""
************************
@author : Gabin
@contact : gabin.mondongou@auxlazaristeslasalle.fr
created on : Tue Mar 21 10:25:51 2023
last mod : 2023
title : notitle
goals : brief description
to do : what should be done next time
************************* """

""" ********************
    **** Imports ****
    ******************** """
# no data

""" ********************
    **** Classes ****
    ******************** """
# no data

""" ********************
    **** Functions ****
    ******************** """
def parcours_profondeur(matrice, debut, visite=None):
    if visite is None:
        visite = set()
    visite.add(debut)
    for voisin in range(len(matrice)):
        if matrice[debut][voisin] == 1 and voisin not in visite:
            parcours_profondeur(matrice, voisin, visite)
    return visite

def connexite(matrice):
    noeud_depart = 0
    accessible = parcours_profondeur(matrice, noeud_depart)
    if len(accessible) == len(matrice) :
        print("Le graphe est connexe")
    else:
        print("Le graphe n'est pas connexe")
   
""" ********************
    **** Global Var ****
    ******************** """
# no data

""" **************
    **** Main ****
    ************** """






