import numpy as np
import random

nodes = ('vitacura', 'lo barnechea', 'las condes', 'la reina', 'providencia', 'nunoa', 'macul','santiago',
         'estacion central','san miguel','san joaquin','penalolen','la florida')

# Estas son los tiempos de viaje entre comunas adyacentes según Maps en horario fuera de punto
tiempos_fdp = {'vitacura': {'vitacura': 11, 'lo barnechea': 15, 'las condes': 15, 'providencia': 19},
            'lo barnechea': {'vitacura': 18, 'lo barnechea': 13 , 'las condes': 16 },
            'las condes': {'vitacura': 26, 'lo barnechea': 25, 'las condes': 18, 'la reina': 15, 'providencia': 20},
            'la reina': {'las condes': 20, 'la reina': 12, 'providencia': 20, 'nunoa': 22, 'penalolen': 15},
            'providencia': {'vitacura': 17, 'las condes': 18, 'la reina': 25, 'providencia': 13, 'nunoa': 11, 'santiago': 20},
            'nunoa': {'la reina': 21, 'providencia': 14, 'nunoa': 14, 'macul': 15, 'santiago': 30, 'san joaquin': 25, 'penalolen': 15},
            'macul': {'nunoa': 13, 'macul': 16,'san joaquin': 17, 'penalolen': 14, 'la florida': 15},
            'santiago': {'providencia': 25, 'nunoa': 30, 'santiago': 18, 'estacion central': 14, 'san miguel': 15, 'san joaquin': 22},
            'estacion central': {'santiago': 16, 'estacion central': 17},
            'san miguel': {'santiago': 20, 'san miguel': 12, 'san joaquin': 7},
            'san joaquin': {'nunoa': 20, 'macul': 12, 'santiago': 21, 'san miguel': 10, 'san joaquin': 14 , 'la florida': 18},
            'penalolen': {'la reina': 15, 'nunoa': 13, 'macul': 16, 'penalolen': 20, 'la florida': 17},
            'la florida': {'macul': 14, 'san joaquin': 15, 'penalolen': 16, 'la florida': 30}}

# tiempos en horario punta, con variabilidad en la media y desv estandar minima.

tiempos_hp ={'vitacura': {'vitacura': (np.random.normal(random.uniform(1.15, 1.35)*11, 2)), 'lo barnechea': (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'las condes': (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'providencia': (np.random.normal(random.uniform(1.15, 1.35)*19, 2))},
            'lo barnechea': {'vitacura': (np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'lo barnechea': (np.random.normal(random.uniform(1.15, 1.35)*13, 2)) , 'las condes': (np.random.normal(random.uniform(1.15, 1.35)*16, 2)) },
            'las condes': {'vitacura': (np.random.normal(random.uniform(1.15, 1.35)*26, 2)), 'lo barnechea': (np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'las condes': (np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'la reina': (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'providencia': (np.random.normal(random.uniform(1.15, 1.35)*20, 2))},
            'la reina': {'las condes': (np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'la reina': (np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'providencia': (np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'nunoa':  (np.random.normal(random.uniform(1.15, 1.35)*22, 2)), 'penalolen':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'providencia': {'vitacura':  (np.random.normal(random.uniform(1.15, 1.35)*17, 2)), 'las condes':  (np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'la reina':  (np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'providencia':  (np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'nunoa':  (np.random.normal(random.uniform(1.15, 1.35)*11, 2)), 'santiago':  (np.random.normal(random.uniform(1.15, 1.35)*20, 2))},
            'nunoa': {'la reina':  (np.random.normal(random.uniform(1.15, 1.35)*21, 2)), 'providencia':  (np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'nunoa': (np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'macul':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'santiago':  (np.random.normal(random.uniform(1.15, 1.35)*30, 2)), 'san joaquin':  (np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'penalolen':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'macul': {'nunoa':  (np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'macul':  (np.random.normal(random.uniform(1.15, 1.35)*16, 2)),'san joaquin':  (np.random.normal(random.uniform(1.15, 1.35)*17, 2)), 'penalolen':  (np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'la florida':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'santiago': {'providencia': (np.random.normal(random.uniform(1.15, 1.35)*25,2)), 'nunoa': (np.random.normal(random.uniform(1.15, 1.35)*30,2)), 'santiago': (np.random.normal(random.uniform(1.15, 1.35)*18,2)), 'estacion central': (np.random.normal(random.uniform(1.15, 1.35)*14,2)), 'san miguel': (np.random.normal(random.uniform(1.15, 1.35)*15,2)), 'san joaquin': (np.random.normal(random.uniform(1.15, 1.35)*22,2))},
            'estacion central': {'santiago':  (np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'estacion central':  (np.random.normal(random.uniform(1.15, 1.35)*17, 2))},
            'san miguel': {'santiago':  (np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'san miguel':  (np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'san joaquin':  (np.random.normal(random.uniform(1.15, 1.35)*7, 2))},
            'san joaquin': {'nunoa':  (np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'macul':  (np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'santiago':  (np.random.normal(random.uniform(1.15, 1.35)*21, 2)), 'san miguel':  (np.random.normal(random.uniform(1.15, 1.35)*10, 2)), 'san joaquin':  (np.random.normal(random.uniform(1.15, 1.35)*14, 2)) , 'la florida':  (np.random.normal(random.uniform(1.15, 1.35)*18, 2))},
            'penalolen': {'la reina':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'nunoa':  (np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'macul':  (np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'penalolen':  (np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'la florida':  (np.random.normal(random.uniform(1.15, 1.35)*17, 2))},
            'la florida': {'macul':  (np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'san joaquin':  (np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'penalolen':  (np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'la florida':  (np.random.normal(random.uniform(1.15, 1.35)*30, 2))}}


def Dijkstra(nodes, tiempos_fdp, current):

    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in tiempos_fdp[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    return visited


def DijkstraVariable(nodo):
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = nodo
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in tiempos_hp[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key= lambda x: x[1])[0]
    return visited

# outputs de los Dijkstras
#tiempos de viaje fuera de punta
tdv_fdp = {}
for comuna in tiempos_fdp.keys():
    tdv_fdp.update({comuna: Dijkstra(nodes, tiempos_fdp, comuna)})
    #print(Dijkstra(nodes, tiempos_fdp, comuna))
#print(tdv_fdp)

#print("\n\n")
#tiempos de viaje horario punta
tdv_hp = {}
for i in nodes:
    tdv_hp.update({i: DijkstraVariable(i)})
    #print(DijkstraVariable(i))

#print(tdv_hp)

# completa los datos de la matriz que genera el Dijkstra, agregando los tiempos del "autoloop"
# o el viaje dentro de la misma zona (vitacura a vitacura)
def completar_matriz(diccionario, tipo):


    for key in diccionario.keys():
        for llave in diccionario[key].keys():
            if key == llave and tipo == 'peak':
                diccionario[key][llave] = tiempos_hp[key][llave]
            elif key == llave and tipo == 'no_peak':
                diccionario[key][llave] = tiempos_fdp[key][llave]
    return diccionario
    #print(f'el tiempo entre {key} y {llave} es de {diccionario[key][llave]} minutos')


completar_matriz(tdv_fdp, 'peak')
completar_matriz(tdv_hp, 'no_peak')

# Necesita que le pases la matriz correspondiente al horario (punta o fuera de punta)
def getTime(matriz,inicio,final):
    tiempo = matriz[inicio][final]
    return tiempo

"""
print(tdv_fdp)
print(tdv_hp)
print(getTime(tdv_hp,   "vitacura","vitacura"))
print(getTime(tdv_fdp,  "vitacura","vitacura"))
print(getTime(tdv_fdp,  "vitacura","san joaquin"))
print(getTime(tdv_hp,   "vitacura","san joaquin"))
"""