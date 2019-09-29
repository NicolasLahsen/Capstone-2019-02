import numpy as np
import random

nodes = ('Vitacura', 'Lo Barnechea', 'Las Condes', 'La Reina', 'Providencia', 'Nunoa', 'Macul','Santiago',
         'Estacion Central','San Miguel','San Joaquin','Penalolen','La Florida')

# Estas son los tiempos de viaje entre comunas adyacentes según Maps en horario fuera de punto
tiempos_fdp = {'Vitacura': {'Vitacura': 11, 'Lo Barnechea': 15, 'Las Condes': 15, 'Providencia': 19},
            'Lo Barnechea': {'Vitacura': 18, 'Lo Barnechea': 13 , 'Las Condes': 16 },
            'Las Condes': {'Vitacura': 26, 'Lo Barnechea': 25, 'Las Condes': 18, 'La Reina': 15, 'Providencia': 20},
            'La Reina': {'Las Condes': 20, 'La Reina': 12, 'Providencia': 20, 'Nunoa': 22, 'Penalolen': 15},
            'Providencia': {'Vitacura': 17, 'Las Condes': 18, 'La Reina': 25, 'Providencia': 13, 'Nunoa': 11, 'Santiago': 20},
            'Nunoa': {'La Reina': 21, 'Providencia': 14, 'Nunoa': 14, 'Macul': 15, 'Santiago': 30, 'San Joaquin': 25, 'Penalolen': 15},
            'Macul': {'Nunoa': 13, 'Macul': 16,'San Joaquin': 17, 'Penalolen': 14, 'La Florida': 15},
            'Santiago': {'Providencia': 25, 'Nunoa': 30, 'Santiago': 18, 'Estacion Central': 14, 'San Miguel': 15, 'San Joaquin': 22},
            'Estacion Central': {'Santiago': 16, 'Estacion Central': 17},
            'San Miguel': {'Santiago': 20, 'San Miguel': 12, 'San Joaquin': 7},
            'San Joaquin': {'Nunoa': 20, 'Macul': 12, 'Santiago': 21, 'San Miguel': 10, 'San Joaquin': 14 , 'La Florida': 18},
            'Penalolen': {'La Reina': 15, 'Nunoa': 13, 'Macul': 16, 'Penalolen': 20, 'La Florida': 17},
            'La Florida': {'Macul': 14, 'San Joaquin': 15, 'Penalolen': 16, 'La Florida': 30}}

# tiempos en horario punta, con variabilidad en la media y desv estandar minima.

tiempos_hp ={'Vitacura': {'Vitacura': round(np.random.normal(random.uniform(1.15, 1.35)*11, 2)), 'Lo Barnechea': round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Las Condes': round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Providencia': round(np.random.normal(random.uniform(1.15, 1.35)*19, 2))},
            'Lo Barnechea': {'Vitacura': round(np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'Lo Barnechea': round(np.random.normal(random.uniform(1.15, 1.35)*13, 2)) , 'Las Condes': round(np.random.normal(random.uniform(1.15, 1.35)*16, 2)) },
            'Las Condes': {'Vitacura': round(np.random.normal(random.uniform(1.15, 1.35)*26, 2)), 'Lo Barnechea': round(np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'Las Condes': round(np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'La Reina': round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Providencia': round(np.random.normal(random.uniform(1.15, 1.35)*20, 2))},
            'La Reina': {'Las Condes': round(np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'La Reina': round(np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'Providencia': round(np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'Nunoa':  round(np.random.normal(random.uniform(1.15, 1.35)*22, 2)), 'Penalolen':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'Providencia': {'Vitacura':  round(np.random.normal(random.uniform(1.15, 1.35)*17, 2)), 'Las Condes':  round(np.random.normal(random.uniform(1.15, 1.35)*18, 2)), 'La Reina':  round(np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'Providencia':  round(np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'Nunoa':  round(np.random.normal(random.uniform(1.15, 1.35)*11, 2)), 'Santiago':  round(np.random.normal(random.uniform(1.15, 1.35)*20, 2))},
            'Nunoa': {'La Reina':  round(np.random.normal(random.uniform(1.15, 1.35)*21, 2)), 'Providencia':  round(np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'Nunoa': round(np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'Macul':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Santiago':  round(np.random.normal(random.uniform(1.15, 1.35)*30, 2)), 'San Joaquin':  round(np.random.normal(random.uniform(1.15, 1.35)*25, 2)), 'Penalolen':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'Macul': {'Nunoa':  round(np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'Macul':  round(np.random.normal(random.uniform(1.15, 1.35)*16, 2)),'San Joaquin':  round(np.random.normal(random.uniform(1.15, 1.35)*17, 2)), 'Penalolen':  round(np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'La Florida':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2))},
            'Santiago': {'Providencia': round(np.random.normal(random.uniform(1.15, 1.35)*25,2)), 'Nunoa': round(np.random.normal(random.uniform(1.15, 1.35)*30,2)), 'Santiago': round(np.random.normal(random.uniform(1.15, 1.35)*18,2)), 'Estacion Central': round(np.random.normal(random.uniform(1.15, 1.35)*14,2)), 'San Miguel': round(np.random.normal(random.uniform(1.15, 1.35)*15,2)), 'San Joaquin': round(np.random.normal(random.uniform(1.15, 1.35)*22,2))},
            'Estacion Central': {'Santiago':  round(np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'Estacion Central':  round(np.random.normal(random.uniform(1.15, 1.35)*17, 2))},
            'San Miguel': {'Santiago':  round(np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'San Miguel':  round(np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'San Joaquin':  round(np.random.normal(random.uniform(1.15, 1.35)*7, 2))},
            'San Joaquin': {'Nunoa':  round(np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'Macul':  round(np.random.normal(random.uniform(1.15, 1.35)*12, 2)), 'Santiago':  round(np.random.normal(random.uniform(1.15, 1.35)*21, 2)), 'San Miguel':  round(np.random.normal(random.uniform(1.15, 1.35)*10, 2)), 'San Joaquin':  round(np.random.normal(random.uniform(1.15, 1.35)*14, 2)) , 'La Florida':  round(np.random.normal(random.uniform(1.15, 1.35)*18, 2))},
            'Penalolen': {'La Reina':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Nunoa':  round(np.random.normal(random.uniform(1.15, 1.35)*13, 2)), 'Macul':  round(np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'Penalolen':  round(np.random.normal(random.uniform(1.15, 1.35)*20, 2)), 'La Florida':  round(np.random.normal(random.uniform(1.15, 1.35)*17, 2))},
            'La Florida': {'Macul':  round(np.random.normal(random.uniform(1.15, 1.35)*14, 2)), 'San Joaquin':  round(np.random.normal(random.uniform(1.15, 1.35)*15, 2)), 'Penalolen':  round(np.random.normal(random.uniform(1.15, 1.35)*16, 2)), 'La Florida':  round(np.random.normal(random.uniform(1.15, 1.35)*30, 2))}}

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


def printear_matriz(diccionario, tipo):

    for key in diccionario.keys():
        for llave in diccionario[key].keys():
            if key == llave and tipo == 'peak':
                diccionario[key][llave] = tiempos_hp[key][llave]
            elif key == llave and tipo == 'no_peak':
                diccionario[key][llave] = tiempos_fdp[key][llave]
            print(f'el tiempo entre {key} y {llave} es de {diccionario[key][llave]} minutos')


printear_matriz(tdv_fdp, 'peak')

printear_matriz(tdv_hp, 'no_peak')
