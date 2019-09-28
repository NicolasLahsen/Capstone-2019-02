import numpy as np

nodes = ('Vitacura', 'Lo Barnechea', 'Las Condes', 'La Reina', 'Providencia', 'Nunoa', 'Macul','Santiago',
         'Estacion Central','San Miguel','San Joaquin','Penalolen','La Florida')
distances ={'Vitacura': {'Vitacura': 11, 'Lo Barnechea': round(np.random.normal(15, 2)), 'Las Condes': round(np.random.normal(15, 2)), 'Providencia': round(np.random.normal(19, 2))},
                      'Lo Barnechea': {'Vitacura': round(np.random.normal(18, 2)), 'Lo Barnechea': round(np.random.normal(13, 2)) , 'Las Condes': round(np.random.normal(16, 2)) },
                      'Las Condes': {'Vitacura': round(np.random.normal(26, 2)), 'Lo Barnechea': round(np.random.normal(25, 2)), 'Las Condes': round(np.random.normal(18, 2)), 'La Reina': round(np.random.normal(15, 2)), 'Providencia': round(np.random.normal(20, 2))},
                      'La Reina': {'Las Condes': round(np.random.normal(20, 2)), 'La Reina': round(np.random.normal(12, 2)), 'Providencia': round(np.random.normal(20, 2)), 'Nunoa':  round(np.random.normal(22, 2)), 'Penalolen':  round(np.random.normal(15, 2))},
                      'Providencia': {'Vitacura':  round(np.random.normal(17, 2)), 'Las Condes':  round(np.random.normal(18, 2)), 'La Reina':  round(np.random.normal(25, 2)), 'Providencia':  round(np.random.normal(13, 2)), 'Nunoa':  round(np.random.normal(11, 2)), 'Santiago':  round(np.random.normal(20, 2))},
                      'Nunoa': {'La Reina':  round(np.random.normal(21, 2)), 'Providencia':  round(np.random.normal(14, 2)), 'Nunoa': round(np.random.normal(14, 2)), 'Macul':  round(np.random.normal(15, 2)), 'Santiago':  round(np.random.normal(30, 2)), 'San Joaquin':  round(np.random.normal(25, 2)), 'Penalolen':  round(np.random.normal(15, 2))},
                      'Macul': {'Nunoa':  round(np.random.normal(13, 2)), 'Macul':  round(np.random.normal(16, 2)),'San Joaquin':  round(np.random.normal(17, 2)), 'Penalolen':  round(np.random.normal(14, 2)), 'La Florida':  round(np.random.normal(15, 2))},
                      'Santiago': {'Providencia': 25, 'Nunoa': 30, 'Santiago': 18, 'Estacion Central': 14, 'San Miguel': 15, 'San Joaquin': 22},
                      'Estacion Central': {'Santiago':  round(np.random.normal(16, 2)), 'Estacion Central':  round(np.random.normal(17, 2))},
                      'San Miguel': {'Santiago':  round(np.random.normal(20, 2)), 'San Miguel':  round(np.random.normal(12, 2)), 'San Joaquin':  round(np.random.normal(7, 2))},
                      'San Joaquin': {'Nunoa':  round(np.random.normal(20, 2)), 'Macul':  round(np.random.normal(12, 2)), 'Santiago':  round(np.random.normal(21, 2)), 'San Miguel':  round(np.random.normal(10, 2)), 'San Joaquin':  round(np.random.normal(14, 2)) , 'La Florida':  round(np.random.normal(18, 2))},
                      'Penalolen': {'La Reina':  round(np.random.normal(15, 2)), 'Nunoa':  round(np.random.normal(13, 2)), 'Macul':  round(np.random.normal(16, 2)), 'Penalolen':  round(np.random.normal(20, 2)), 'La Florida':  round(np.random.normal(17, 2))},
                      'La Florida': {'Macul':  round(np.random.normal(14, 2)), 'San Joaquin':  round(np.random.normal(15, 2)), 'Penalolen':  round(np.random.normal(16, 2)), 'La Florida':  round(np.random.normal(30, 2))}}

def Dijstrak(nodo):
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = nodo
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited

for i in nodes:
    print(Dijstrak(i))