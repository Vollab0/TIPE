from Algo_PCC import dijkstra_mat
from Algo_PCC import dijkstra_dic
from Algo_PCC import mat_to_dico
from Algo_PCC import Astar
from Main import matrice
from Main import liste_stations_matrice
import numpy as np
import time



mat=np.array([[0,1,2,0,0],
              [0,0,0,3,0],
              [0,0,0,1,0],
              [0,0,0,0,3],
              [0,2,1,0,0]])

dico=mat_to_dico(matrice)

print(dijkstra_mat(matrice,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux')))
duree1=0
for i in range(10000):
    tac = time.time()
    dijkstra_mat(matrice,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux'))
    duree1+=time.time()-tac
print('M',duree1)

dico=mat_to_dico(matrice)

print(dijkstra_dic(dico,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux')))
duree2=0
for i in range(10000):
    tac = time.time()
    dijkstra_dic(dico,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux'))
    duree2+=time.time()-tac
print('D',duree2)

print(Astar(matrice,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux')))
duree3=0
for i in range(10000):
    tac = time.time()
    Astar(matrice,liste_stations_matrice.index('Cuire'),liste_stations_matrice.index('Brotteaux'))
    duree3+=time.time()-tac
print('A',duree3)

"""
print(liste_stations_matrice)
"""

