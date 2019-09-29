nodos = ('Vitacura', 'Lo Barnechea', 'Las Condes', 'La Reina', 'Providencia', 'Nunoa', 'Macul','Santiago',
         'Estacion Central','San Miguel','San Joaquin','Penalolen','La Florida')
distancias_adyacentes ={'Vitacura': {'Vitacura': 11, 'Lo Barnechea': 15, 'Las Condes': 15, 'Providencia': 19},
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

distancias_totales = dict()
for nodo in nodos:
    unvisited = {node: None for node in nodos}  # using None as +inf
    visited = {}
    current = nodo
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distancias_adyacentes[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    distancias_totales[nodo] = visited

for comuna in distancias_totales:
    distancias_totales[comuna][comuna] = distancias_adyacentes[comuna][comuna]

media_tiempos_entre_comunas = {'Vitacura': {'Vitacura': 11, 'Lo Barnechea': 15, 'Las Condes': 15, 'Providencia': 19, 'La Reina': 30, 'Nunoa': 30, 'Santiago': 39, 'Macul': 45, 'Penalolen': 45, 'Estacion Central': 53, 'San Miguel': 54, 'San Joaquin': 55, 'La Florida': 60},
              'Lo Barnechea': {'Lo Barnechea': 13, 'Las Condes': 16, 'Vitacura': 18, 'La Reina': 31, 'Providencia': 36, 'Penalolen': 46, 'Nunoa': 47, 'Santiago': 56, 'Macul': 62, 'La Florida': 63, 'Estacion Central': 70, 'San Miguel': 71, 'San Joaquin': 72},
              'Las Condes': {'Las Condes': 18, 'La Reina': 15, 'Providencia': 20, 'Lo Barnechea': 25, 'Vitacura': 26, 'Penalolen': 30, 'Nunoa': 31, 'Santiago': 40, 'Macul': 46, 'La Florida': 47, 'Estacion Central': 54, 'San Miguel': 55, 'San Joaquin': 56},
              'La Reina': {'La Reina': 12, 'Penalolen': 15, 'Las Condes': 20, 'Providencia': 20, 'Nunoa': 22, 'Macul': 31, 'La Florida': 32, 'Vitacura': 37, 'Santiago': 40, 'Lo Barnechea': 45, 'San Joaquin': 47, 'Estacion Central': 54, 'San Miguel': 55},
              'Providencia': {'Providencia': 13, 'Nunoa': 11, 'Vitacura': 17, 'Las Condes': 18, 'Santiago': 20, 'La Reina': 25, 'Macul': 26, 'Penalolen': 26, 'Lo Barnechea': 32, 'Estacion Central': 34, 'San Miguel': 35, 'San Joaquin': 36, 'La Florida': 41},
              'Nunoa': {'Nunoa': 14, 'Providencia': 14, 'Macul': 15, 'Penalolen': 15, 'La Reina': 21, 'San Joaquin': 25, 'Santiago': 30, 'La Florida': 30, 'Vitacura': 31, 'Las Condes': 32, 'San Miguel': 35, 'Estacion Central': 44, 'Lo Barnechea': 46},
              'Macul': {'Macul': 16, 'Nunoa': 13, 'Penalolen': 14, 'La Florida': 15, 'San Joaquin': 17, 'Providencia': 27, 'San Miguel': 27, 'La Reina': 29, 'Santiago': 38, 'Vitacura': 44, 'Las Condes': 45, 'Estacion Central': 52, 'Lo Barnechea': 59},
              'Santiago': {'Santiago': 18, 'Estacion Central': 14, 'San Miguel': 15, 'San Joaquin': 22, 'Providencia': 25, 'Nunoa': 30, 'Macul': 34, 'La Florida': 40, 'Vitacura': 42, 'Las Condes': 43, 'Penalolen': 45, 'La Reina': 50, 'Lo Barnechea': 57},
              'Estacion Central': {'Estacion Central': 17, 'Santiago': 16, 'San Miguel': 31, 'San Joaquin': 38, 'Providencia': 41, 'Nunoa': 46, 'Macul': 50, 'La Florida': 56, 'Vitacura': 58, 'Las Condes': 59, 'Penalolen': 61, 'La Reina': 66, 'Lo Barnechea': 73},
              'San Miguel': {'San Miguel': 12, 'San Joaquin': 7, 'Macul': 19, 'Santiago': 20, 'La Florida': 25, 'Nunoa': 27, 'Penalolen': 33, 'Estacion Central': 34, 'Providencia': 41, 'La Reina': 48, 'Vitacura': 58, 'Las Condes': 59, 'Lo Barnechea': 73},
              'San Joaquin': {'San Joaquin': 14, 'San Miguel': 10, 'Macul': 12, 'La Florida': 18, 'Nunoa': 20, 'Santiago': 21, 'Penalolen': 26, 'Providencia': 34, 'Estacion Central': 35, 'La Reina': 41, 'Vitacura': 51, 'Las Condes': 52, 'Lo Barnechea': 66},
              'Penalolen': {'Penalolen': 20, 'Nunoa': 13, 'La Reina': 15, 'Macul': 16, 'La Florida': 17, 'Providencia': 27, 'San Joaquin': 32, 'Las Condes': 35, 'San Miguel': 42, 'Santiago': 43, 'Vitacura': 44, 'Estacion Central': 57, 'Lo Barnechea': 59},
              'La Florida': {'La Florida': 30, 'Macul': 14, 'San Joaquin': 15, 'Penalolen': 16, 'San Miguel': 25, 'Nunoa': 27, 'La Reina': 31, 'Santiago': 36, 'Providencia': 41, 'Estacion Central': 50, 'Las Condes': 51, 'Vitacura': 58, 'Lo Barnechea': 73}}






