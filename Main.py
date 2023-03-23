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
from kivy.properties import ListProperty
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import AsyncImage
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout    
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.size = (540, 1080)


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

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class Application(MDApp):

    resultat = StringProperty() # Provisoire
    zone_texte_destination = ObjectProperty(None)
    zone_texte_depart = ObjectProperty(None)

    dico_changements = ObjectProperty(None)
    distance = ObjectProperty(None)
    chemin = ListProperty(['depart'])



    def build(self):

        self.theme_cls = ThemeManager()

        self.root = ScreenManager() # Gestion des differentes pages
        self.root.add_widget(Builder.load_file('page_principale.kv')) # Charge le premier ecran test.kv
        self.root.add_widget(Builder.load_file('page_resultats.kv')) # Charge le premier ecran test.kv

        stations_clees = list(stations_infos.keys())
        stations_triees = sorted(stations_clees)

        liste_choix_station_depart = [
            {
                "viewclass": "IconListItem",
                "icon": "Images/Metro.png",
                "text": station,
                "height": 50,
                "font_name": 'SPoppins',
                "on_release": lambda x=station: self.nom_station_depart(x),
            } for station in stations_triees
        ]
        liste_choix_station_arrivee = [
            {
                "viewclass": "IconListItem",
                "icon": "Images/Metro.png",
                "text": station,
                "height": 50,
                "font_name": 'SPoppins',
                "on_release": lambda x=station: self.nom_station_arrivee(x),
            } for station in stations_triees
        ]
        self.menu_station_depart = MDDropdownMenu(
            caller = self.root.get_screen('main').ids.choix_station_depart,
            items = liste_choix_station_depart,
            position = "center",
            hor_growth=None,
            ver_growth="down",
            width_mult = 4,
        )
        self.menu_station_arrivee = MDDropdownMenu(
            caller = self.root.get_screen('main').ids.choix_station_arrivee,
            items = liste_choix_station_arrivee,
            position = "center",
            hor_growth=None,
            ver_growth="down",
            width_mult = 4,
        )
        

        return self.root # Affiche les pages
    
    def nom_station_depart(self, nom): # Cette fonction met a jour dynamiquement le nom de la station choisie et ferme le menu
        page_principale = self.root.get_screen('main')
        page_principale.ids.choix_station_depart.text = nom
        self.item_depart = nom
        self.menu_station_depart.dismiss()
    
    def nom_station_arrivee(self, nom): # Cette fonction met a jour dynamiquement le nom de la station choisie et ferme le menu
        page_principale = self.root.get_screen('main')
        page_principale.ids.choix_station_arrivee.text = nom
        self.item_arrivee = nom
        self.menu_station_arrivee.dismiss()

    def inverser_stations(self):
        page_principale = self.root.get_screen('main')
        page_principale.ids.choix_station_arrivee.text,page_principale.ids.choix_station_depart.text = page_principale.ids.choix_station_depart.text,page_principale.ids.choix_station_arrivee.text


    def afficher_resultats(self):
        ligne_layout = self.root.get_screen('resultat').ids.ligne_layout
        ligne_layout.clear_widgets()

        ligne_precedente = ''

        for key, value in self.dico_changements.items():
            
            if ligne_precedente != value[0]:

                image = AsyncImage(source='Images/LigneMetro'+ str(value[0]) + '.png')

                image.texture_size = (100, 100)
                image.size_hint = (None, None)



                if len(self.dico_changements.keys()) == 2 :
                    image.width = 150
                    image.height = 150
                    image.pos_hint = {'center_x':.58, 'center_y': .5}
                
                elif len(self.dico_changements.keys()) == 1 :
                    image.width = 200
                    image.height = 200
                    image.pos_hint = {'center_x':.58, 'center_y': .2}

                elif len(self.dico_changements.keys()) == 3 :
                    image.width = 120
                    image.height = 120
                    image.pos_hint = {'center_x':.56, 'center_y': .5}

                ligne_layout.add_widget(image)

            
            label = MDLabel(text=key)

            label.pos_hint = {'center_x':.5}
            label.halign = 'center'
            label.font_name = 'MPoppins'
            
            image2 = AsyncImage(source='Images/LigneMetro'+ str(value[1]) + '.png')

            image2.texture_size = (100, 100)
            image2.size_hint = (None, None)

            if len(self.dico_changements.keys()) == 2 :
                image2.width = 150
                image2.height = 150
                label.font_size = '20dp'
                image2.pos_hint = {'center_x':.58, 'center_y': .5}
            
            elif len(self.dico_changements.keys()) == 1 :
                image2.width = 200
                image2.height = 200
                label.font_size = '30dp'
                image2.pos_hint = {'center_x':.58, 'center_y': .8}

            elif len(self.dico_changements.keys()) == 3 :
                image2.width = 120
                image2.height = 120
                label.font_size = '15dp'
                image2.pos_hint = {'center_x':.56, 'center_y': .5}

            ligne_layout.add_widget(label)
            ligne_layout.add_widget(image2)

            ligne_precedente = value[1] 


        if len(self.dico_changements.keys()) == 0 :

            lignes_passant_par_la_station_de_depart = appartenance_ligne(self.chemin[0])  
            lignes_passant_par_la_station_d_arrive = appartenance_ligne(self.chemin[-1]) 

            for el in lignes_passant_par_la_station_de_depart:
                if el in lignes_passant_par_la_station_d_arrive:
                    ligne_en_commun = el

            image = AsyncImage(source='Images/LigneMetro'+ str(ligne_en_commun) + '.png')

            image.texture_size = (100, 100)
            image.size_hint = (None, None)
            image.width = 200
            image.height = 200
            image.pos_hint = {'center_x':.58, 'center_y': .5}

            ligne_layout.add_widget(image)



    def rechercher(self): # Renvoie le resultat de la recherche
        
        depart = self.item_depart
        destination = self.item_arrivee

        self.chemin,self.distance,self.dico_changements = recherche_itineraire(depart,destination)

        # self.resultat = str(self.chemin) # Provisoire

        self.root.transition.direction = 'left'
        self.root.current = 'resultat'

        self.afficher_resultats()

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


# PROBLEME : La station Henon ne semble pas exister...
# Ajouter les funi


