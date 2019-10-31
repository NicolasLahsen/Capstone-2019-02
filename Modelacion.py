import random
from numpy import mean
from collections import deque
from itertools import count


class Simulacion:
    def __init__(servidores: list, tiempo: float, eventos: list(tuple))
    self.servidores = servidores
    self.tiempo = tiempo
    self.eventos = [lambda x:x[1] == "contestar_llamada", eventos]


class Servidor:
    classcounter = 0

    def __init__(self, nombre, tiempo=0):
        self.id_ = Servidor.classcounter
        self.libre = True
        self.tiempo = tiempo
        Servidor.classcounter += 1

    def llegada_llamada(self, tiempo):
        self.libre = False
        print(f"Ha llegado un llamada a el servidor {self.id_} en {tiempo}")
        self.tiempo = tiempo

    def salida_llamada(self):
        self.libre = True
        self.tiempo = self.tiempo + random.uniform(0.5, 1.5)
        print(f"el servidor {self.nombre} ha quedado disponible en {self.tiempo}")


def atender_llamada(llamadas, servidor, atendidos):
    servidor.llegada_llamada(llamadas[0].tiempo_llegada)
    servidor.salida_llamada(llamadas[0])
    atendidos.append(llamadas[0])
    if len(llamadas > 0):
        llamadas.pop(0)
    else:
        pass


def rechazar_llamada(llamadas, rechazados):
    rechazados.append(llamadas[0])
    llamadas.pop(0)


def run(l_servidors, cola, rechazados, atendidos):
    tiempo_llegadas = crear_eventos()
    llamadas = [llamada(i) for i in tiempo_llegadas]
    for iterador in range(1000):
        # aun no atendemos a nadie
        atendido = False
        # Llega un llamada
        llegada = llamadas[0]
        # Si hay servidor disponible en su llegada
        for servidor in l_servidors:
            # Vemos si hay servidors disponibles cuando llega
            if servidor.libre and servidor.tiempo < llegada.tiempo_llegada:
                # Si no hay cola, lo atienden
                if len(cola) == 0:
                    servidor.llegada_llamada(llegada.tiempo_llegada)
                    servidor.salida_llamada()
                    llegada.tiempo_salida = servidor.tiempo
                    atendidos.append(llegada)
                    atendido = True
                    break
        # Si estan todas las servidors ocupadas en ese momento y no atendimos a nadie

    print(
        f"Se atendieron {len(atendidos)} llamadas, se perdieron {len(rechazados)} llamadas de las 1000 llamadas en {max(servidor1.tiempo,servidor2.tiempo,servidor3.tiempo,servidor4.tiempo)} minutos")


# CORRE


Lista_tasa_media = []
Lista_llamadas_rechazados = []
Grafico_tiempo = []
Lista_tiempo_termino = []

for i in range(50):
    servidor1 = Servidor(1)
    servidor2 = Servidor(2)
    servidor3 = Servidor(3)
    servidor4 = Servidor(4)

    l_servidors = [servidor1, servidor2, servidor3, servidor4]
    cola = []
    rechazados = []
    atendidos = []

    run(l_servidors, cola, rechazados, atendidos)

    Lista_tasa_media.append(len(atendidos) / 1000)
    Lista_llamadas_rechazados.append(len(rechazados))
    Lista_tiempo_termino.append(
        max(servidor1.tiempo, servidor2.tiempo, servidor3.tiempo, servidor4.tiempo))

print(f"El promedio de las tasas medias fue: {mean(Lista_tasa_media)}")
print(f"El promedio de llamadas perdidos fue: {mean(Lista_llamadas_rechazados)}")
print(f"En total se perdieron {sum(Lista_llamadas_rechazados)}")
