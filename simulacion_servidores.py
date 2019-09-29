import random
from numpy import mean
from collections import deque
from itertools import count
from Clase_Falla import Falla
from operator import attrgetter
from sty import fg


def hora_a_minuto(hora: str):
    '''
    Recibe string tipo HH:MM y entrega un int de minuto
    '''
    return int(hora[0:1])*60+int(hora[3:4])


class Simulacion:
    def __init__(self, servidores: int, eventos: list):
        self.servidores = [Servidor(self) for i in range(servidores)]
        self.eventos = list(
            filter(lambda x: x[1] == "contestar_llamada", eventos))
        self.output = list(
            filter(lambda x: x[1] != "contestar_llamada", eventos))
        self.tiempo = 0

    def actualizar_servidores(self, tiempo):
        for servidor in self.servidores:
            servidor.actualizar_servidor(tiempo)
        

    def run(self):
        for evento in self.eventos:
            self.actualizar_servidores(evento[0].hora_llamada)
            for servidor in self.servidores:
                if not(servidor.falla):          # Reviso cada servidor
                    # Le asigno la falla a la llamada
                    servidor.llegada_falla(evento[0], evento[0].hora_llamada)
                    self.tiempo = evento[0].hora_llamada
                    break
            else:                            # Si no hay servidores disponibe
                min_t = min(self.servidores, key=attrgetter('falla.hora_salida_callcenter'))
                self.tiempo = min_t.falla.hora_salida_callcenter
                self.actualizar_servidores(min_t.falla.hora_salida_callcenter)
                for servidor in self.servidores:
                    if not(servidor.falla):
                        servidor.llegada_falla(evento[0], self.tiempo)
        max_t = max(list(filter(lambda x: x.falla, self.servidores)), key=attrgetter('falla.hora_salida_callcenter'))
        self.actualizar_servidores(max_t.falla.hora_salida_callcenter)
                

class Servidor:
    classcounter = 0

    def __init__(self, simulacion: Simulacion, falla: Falla = None):
        self.id_ = Servidor.classcounter
        self.falla = None
        self.simulacion = simulacion
        Servidor.classcounter += 1

    def llegada_falla(self, falla, tiempo):
        self.falla = falla
        self.falla.hora_entrada_callcenter = tiempo
        self.falla.hora_salida_callcenter = tiempo + self.falla.tiempo_callcenter
        print(f"Ha llegado una{fg.red} FALLA{fg.rs} al servidor {fg.blue}{self.id_}{fg.rs} en {fg.blue}{str(self.falla.hora_entrada_callcenter)}{fg.rs}, generada en {fg.blue}{str(self.falla.hora_llamada)}{fg.rs}")

    def salida_falla(self):
        self.simulacion.output.append(
            (self.falla, "asignar_tecnico"))  # actualizo el output
        print(f"El servidor {fg.blue}{self.id_}{fg.rs} ha quedado {fg.green}DISPONIBLE{fg.rs} en {fg.blue}{self.falla.hora_salida_callcenter}{fg.rs}")
        self.falla = None  # Libera el servidor

    def actualizar_servidor(self, tiempo):
        if self.falla and self.falla.hora_salida_callcenter <= tiempo:
            self.salida_falla()

    def __str__(self):
        return (f"Servidor {self.id_}, esta atendiendo {self.falla}")


eventos = [(Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 500.62526), "recibir wea"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"),
        (Falla("[comuna]", "[dia]", 480.565), "contestar_llamada"), 
        (Falla("[comuna]", "[dia]", 490.2365), "contestar_llamada")]


sim = Simulacion(5, eventos)
sim.run()
