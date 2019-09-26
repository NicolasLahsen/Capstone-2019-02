import random
class Falla:
    def __init__(self, comuna, hora_llamada):
        self.comuna = comuna
        self.hora_llamada = hora_llamada
        self.tipo = None
        self.grupo = None
        self.tiempo_atencion = None
        self.tiempo_salida = None  #Tiempo de salida de callcenter
        self.definir_tipo()
        self.definir_grupo()

    def definir_tipo(self):
        probabilidad = random.randint(0,100)
        if probabilidad <= 5:
            self.tipo = 1
        elif 5 < probabilidad <= 13:
            self.tipo = 2
        elif 13 < probabilidad <= 23:
            self.tipo = 3
        elif 23 <  probabilidad <= 41:
            self.tipo = 4
        elif 41 < probabilidad <= 53:
            self.tipo = 5
        elif 53 < probabilidad <= 63:
            self.tipo = 6
        elif 63 < probabilidad <= 78:
            self.tipo = 7
        elif 78 < probabilidad:
            self.tipo = 8

    def definir_grupo(self):
        if self.tipo in [1, 4, 8]:
            self.grupo = 'A'
        elif self.tipo in [3, 5, 7]:
            self.grupo = 'B'
        else:
            self.grupo = 'C'


