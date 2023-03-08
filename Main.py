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
import sys

from Recuperation_donnees import recup
from Matrice_adjacence import creation_matrice
from Algo_Dijkstra import plus_court_chemin
from Changements import changements


from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.size = (540, 1200)

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

def recherche_itineraire(depart,destination): # Renvoie le dictionnaire des changements, le chemin et la distance entre le depart et la destination 
    chemin_indices,distance = plus_court_chemin(matrice, liste_stations_matrice.index(depart), liste_stations_matrice.index(destination))
    chemin = [liste_stations_matrice[el] for el in chemin_indices]
    dico_changements = changements(chemin,appartenance_ligne)
    return chemin,distance,dico_changements # dico_changement = {station : [ligne d'arrivé,ligne de départ]}



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

class Application(MDApp):

    resultat = StringProperty() # Provisoire
    zone_texte_destination = ObjectProperty(None)
    zone_texte_depart = ObjectProperty(None)

    dico_changements = DictProperty()
    distance = ObjectProperty(None)
    chemin = ObjectProperty(None)


    def build(self):

        self.theme_cls = ThemeManager()

        gestion_pages = ScreenManager() # Gestion des differentes pages
        gestion_pages.add_widget(Builder.load_file('page_principale.kv')) # Charge le premier ecran test.kv
        gestion_pages.add_widget(Builder.load_file('page_resultats.kv')) # Charge le premier ecran test.kv

        
        return gestion_pages # Affiche les pages
    
    def rechercher(self):
        
        page_principale = self.root.get_screen('main')

        depart = page_principale.ids.zone_texte_depart.text
        destination = page_principale.ids.zone_texte_destination.text

        self.chemin,self.distance,self.dico_changements = recherche_itineraire(depart,destination)

        self.resultat = str(self.chemin) # Provisoire

        print("Le chemin le plus court pour aller de " + depart + " à " + destination + " est " + str(self.chemin) + " et il fait " + str(self.distance) + " km.\n\nIl y a " + str(len(self.dico_changements.keys())) + " changements :")
        for el in self.dico_changements.keys() :
            print("- à " + el + " du métro " + self.dico_changements[el][0] + " au métro " + self.dico_changements[el][1])
        

    def quitter(self):
        sys.exit()

if __name__ == "__main__":
    LabelBase.register("RPoppins", "Poppins/Poppins-Regular.ttf") # initialise la police de caractère
    LabelBase.register("MPoppins", "Poppins/Poppins-Medium.ttf") # initialise la police de caractère
    LabelBase.register("BPoppins", "Poppins/Poppins-SemiBold.ttf") # initialise la police de caractère
    Application().run()
