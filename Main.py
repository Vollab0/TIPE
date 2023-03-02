# -*- coding: utf-8 -*-
"""
************************
@author : Gabin
@contact : gabin.mondongou@auxlazaristeslasalle.fr
created on : Tue Jan 10 22:18:18 2023
last mod : 2022
title : notitle
goals : brief description
to do : what should be done next time
************************* """

""" ********************
    **** Imports ****
    ******************** """

from Recuperation_donnees import recup
from Matrice_adjacence import creation_matrice
from Algo_Dijkstra import plus_court_chemin
from Changements import changements


""" ********************
    **** Classes ****
    ******************** """
# no data

""" ********************
    **** Functions ****
    ******************** """
    
def appartenance_ligne(station): # Renvoie les lignes auquelles appartient la station
    assert type(station) == str , 'Cette fonction ne prend que des chaines de caractères en arguments'
    ligne = [ligne for ligne in list(lignes_infos.keys()) if station in lignes_infos[ligne]['stations']]
    return ligne

""" ********************
    **** Global Var ****
    ******************** """

lien_lignes = "https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=tcl_sytral.tcllignemf_2_0_0&outputFormat=application/json; subtype=geojson&SRSNAME=EPSG:3946&startIndex=0&count=100"
lien_arrets = "https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=tcl_sytral.tclarret&outputFormat=application/json; subtype=geojson&SRSNAME=EPSG:3946&startIndex=0&count=4657"

stations_infos,lignes_infos,codes_lignes = recup(lien_lignes, lien_arrets)

matrice,liste_stations_matrice = creation_matrice(lignes_infos, stations_infos)

""" **************
    **** Main ****
    ************** """

arrivee = input ("A quelle station aller ? \n")
depart = input ("De quelle station partir ? \n")


chemin_indices,distance = plus_court_chemin(matrice, liste_stations_matrice.index(depart), liste_stations_matrice.index(arrivee))

chemin = [liste_stations_matrice[el] for el in chemin_indices]

changements = changements(chemin,stations_infos,appartenance_ligne)

print("Le chemin le plus court pour aller de " + depart + " à " + arrivee + " est " + str(chemin) + " et il fait " + str(distance) + " km.\n\nIl y a " + str(len(changements.keys())) + " changements :")
for el in changements.keys() :
    print("- à " + el + " du métro " + changements[el][0] + " au métro " + changements[el][1])
