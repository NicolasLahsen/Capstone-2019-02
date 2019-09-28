import networkx as nx
import matplotlib.pyplot as plt

tiempos_adyacentes = {'Vitacura': {'Vitacura': 11, 'Lo Barnechea': 15, 'Las Condes': 15, 'Providencia': 19},
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
Posiciones={'Lo Barnechea':(0,0),"Las Condes":(20,0),"Vitacura":(0,20),"La Reina":(40,0),
            "Nunoa":(40,20),"Penalolen":(60,0),"La Florida":(80,20),"Macul":(60,20),
            "Santiago":(20,40),"Estacion Central":(0,40),"San Miguel":(20,50),
            "San Joaquin":(50,40),"Providencia":(20,20)}


N=dict()
Nodos=list()
Arcos=list()
Distancia=dict()
for key in tiempos_adyacentes.keys():
    N[key]= key
    for llave in tiempos_adyacentes[key].keys():
        Nodos.append(key)
        Arcos.append([key,llave])
        if key != llave:
            Distancia[(key,llave)]= tiempos_adyacentes[key][llave]
            print(f'el tiempo entre {key} y {llave} es de {tiempos_adyacentes[key][llave]} minutos')

G = nx.DiGraph()
for i in N.keys():
    G.add_node(N[i],pos= Posiciones[i])
pos = nx.get_node_attributes(G,'pos')
nx.draw_networkx_nodes(G,pos,nodelist=N,node_color='y',node_size=900,alpha=1)
nx.draw_networkx_edges(G,pos,edgelist=Arcos,width=2,alpha=0.5,edge_color='k')
nx.draw_networkx_labels(G,pos,N,font_size=6,font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels = Distancia, label_pos =0.3,rotate=False,font_size =7)
plt.axis('off')
plt.title('Grafo Comunas Adyacentes')
plt.show()


