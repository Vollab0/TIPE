from Algo_PCC import dijkstra_mat
from Algo_PCC import dijkstra_dic
from Main import matrice
from Main import liste_stations_matrice
import numpy as np
import time



mat=np.array([[0,1,2,0,0],
              [0,0,0,3,0],
              [0,0,0,1,0],
              [0,0,0,0,3],
              [0,2,1,0,0]])

tac = time.time()
print(dijkstra_mat(mat,0,4))
print(time.time()-tac)

tac = time.time()
print(dijkstra_dic(mat,0,4))
print(time.time()-tac)

tac = time.time()
print(dijkstra_mat(matrice,liste_stations_matrice.index('Gare de Vaise'),liste_stations_matrice.index('Parilly')))
print(time.time()-tac)

tac = time.time()
print(dijkstra_dic(matrice,liste_stations_matrice.index('Gare de Vaise'),liste_stations_matrice.index('Parilly')))
print(time.time()-tac)

