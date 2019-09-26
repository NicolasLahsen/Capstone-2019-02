nodes = ('Vitacura', 'Lo Barnechea', 'Las Condes', 'La Reina', 'Providencia', 'Nunoa', 'Macul','Santiago',
         'Estacion Central','San Miguel','San Joaquin','Penalolen','La Florida')
distances ={'Vitacura': {'Vitacura': 11, 'Lo Barnechea': 15, 'Las Condes': 15, 'Providencia': 19},
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

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'Vitacura'
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

print(visited)