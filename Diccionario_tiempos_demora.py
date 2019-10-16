diccionario_tiempos_esperados = dict()
medias_gamas = [15, 21, 8, 16, 21, 20, 18, 16]
medias_normales = [(55, 120), (90, 140), (100, 80), (45, 120), (35, 150), (70, 120), (120, 135), (45, 120)]
probabilidades = [0.8, 0.03, 0.05, 0.87, 0.92, 0.15, 0.25, 0.17]

for falla in range(8):
     diccionario = {'tiempo_esperado': medias_gamas[falla] + medias_normales[falla][0] * (1-probabilidades[falla]) + medias_normales[falla][1] * probabilidades[falla],
                    'tiempo_ajuste': medias_normales[falla][0],
                    'tiempo_recambio': medias_normales[falla][1]}
     diccionario_tiempos_esperados[falla] = diccionario

print(diccionario_tiempos_esperados)