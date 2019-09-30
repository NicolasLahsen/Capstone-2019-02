import random
import numpy as np


# trabajar con strings el tema de las horas
def addMin(dia_inicial, hora_inicial, minutos_por_agregar):
    dia = dia_inicial
    h_i_sep = hora_inicial.split(":")
    hora = int(h_i_sep[0])
    minutos = int(h_i_sep[1])
    hora += minutos_por_agregar // 60
    if hora >= 24:
        hora = minutos_por_agregar// 60
        if dia == 'lunes':
            dia = 'martes'
        elif dia == 'martes':
            dia = 'miercoles'
        elif dia == 'miercoles':
            dia = 'jueves'
        elif dia == 'jueves':
            dia = 'viernes'
        else:
            dia = 'sabado'
    minutos = minutos - (minutos // 60) * 60
    string = f'{str(hora).zfill(2)}:{str(minutos).zfill(2)}'
    return dia, string


class Falla:

    class_counter = 0

    def __init__(self, comuna, dia_llamada, hora_llamada):

        self.tipo = None
        self.grupo = None
        self.personal = None
        self.es_recambio = None

        self.comuna = comuna
        self.hora_llamada = hora_llamada  # hora cuando se genero la llamada
        self.dia_llamada = dia_llamada  # dia en que se genero la llamada

        self.hora_entrada_callcenter = None  # OJO: no siempre entraría al call center al mi
        self.tiempo_callcenter = None  # tiempo que pasa en callcenter
        self.hora_salida_callcenter = 0  # hora de salida de callcenter
        self.hora_atencion = None  # hora en que llega a la casa
        self.tiempo_atencion = None  # tiempo que demora desde que le dan el llamado hasta  llegar a la casa
        self.hora_diagnostico = None  # hora en que termina de diagnosticar la falla
        self.tiempo_diagnostico = None  # tiempo que se demora en diagnosticar la falla
        self.hora_resolucion = None  # hora en que termina el llamado
        self.tiempo_resolucion = None  # tiempo que se demora en resolver el problema / AJUSTE O RECAMBIO
        self.minutos = hora_llamada
        self.estado = None
        self.tiempo_total = 0
        self.minuto_inicial = hora_llamada
        self.id = Falla.class_counter
        Falla.class_counter += 1
        #self.minutos_totales()
        self.definir_tipo()
        self.definir_grupo()
        self.definir_tiempos_prob()


    # define qué tipo de grupo
    def definir_tipo(self):
        probabilidad_tipo_falla = random.randint(0,100)
        probabilidad_es_recambio = random.randint(0,100)
        if probabilidad_tipo_falla <= 5:
            self.tipo = 1
            self.personal = 1
            if probabilidad_es_recambio <= 80:
                self.es_recambio = True

        elif 5 < probabilidad_tipo_falla <= 13:
            self.tipo = 2
            self.personal = 1
            if probabilidad_es_recambio <= 3:
                self.es_recambio = True

        elif 13 < probabilidad_tipo_falla <= 23:
            self.tipo = 3
            self.personal = 1
            if probabilidad_es_recambio <= 5:
                self.es_recambio = True
        elif 23 <  probabilidad_tipo_falla <= 41:
            self.tipo = 4
            self.personal = 2
            if probabilidad_es_recambio <= 87:
                self.es_recambio = True
        elif 41 < probabilidad_tipo_falla <= 53:
            self.tipo = 5
            self.personal = 1
            if probabilidad_es_recambio <= 92:
                self.es_recambio = True
        elif 53 < probabilidad_tipo_falla <= 63:
            self.tipo = 6
            self.personal = 2
            if probabilidad_es_recambio <= 15:
                self.es_recambio = True
        elif 63 < probabilidad_tipo_falla <= 78:
            self.tipo = 7
            self.personal = 1
            if probabilidad_es_recambio <= 25:
                self.es_recambio = True
        elif 78 < probabilidad_tipo_falla:
            self.tipo = 8
            self.personal = 1
            if probabilidad_es_recambio <= 17:
                self.es_recambio = True

    def definir_grupo(self):
        if self.tipo in [1, 4, 8]:
            self.grupo = 'A'
            self.tiempo_callcenter = np.random.gamma(5, 2)
        elif self.tipo in [3, 5, 7]:
            self.grupo = 'B'
            self.tiempo_callcenter = np.random.gamma(4.5, 2.5)
        else:
            self.grupo = 'C'
            self.tiempo_callcenter = np.random.gamma(4, 2)

    # t_ajuste distribuyen normal
    # t_recambio distribuye normal
    # t_diagnostico distribuye gammma
    def definir_tiempos_prob(self):

        if self.tipo == 1:

            self.tiempo_diagnostico = np.random.gamma(15, 1)
            if self.es_recambio:
                # t de recambio
                self.tiempo_resolucion = np.random.normal(120, 20)
            else:
                # t de ajuste
                self.tiempo_resolucion = np.random.normal(55, 10)

        elif self.tipo == 2:
            self.tiempo_diagnostico = np.random.gamma(7, 3)
            if self.es_recambio:
                self.tiempo_resolucion = np.random.normal(140, 25)

            else:
                self.tiempo_resolucion = np.random.normal(90, 20)

        elif self.tipo == 3:
            self.tiempo_diagnostico = np.random.gamma(8, 1)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(100, 15)
            else:
                self.tiempo_resolucion = np.random.normal(80, 8)

        elif self.tipo == 4:
            self.tiempo_diagnostico = np.random.gamma(8, 2)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(45, 5)
            else:
                self.tiempo_resolucion = np.random.normal(120, 20)

        elif self.tipo == 5:
            self.tiempo_diagnostico = np.random.gamma(7, 3)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(35, 4)
            else:
                self.tiempo_resolucion = np.random.normal(150, 30)

        elif self.tipo == 6:
            self.tiempo_diagnostico = np.random.gamma(10, 2)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(70, 8)
            else:
                self.tiempo_resolucion = np.random.normal(120, 25)

        elif self.tipo == 7:
            self.tiempo_diagnostico = np.random.gamma(9, 2)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(120, 15)
            else:
                self.tiempo_resolucion = np.random.normal(135, 24)

        elif self.tipo == 8:
            self.tiempo_diagnostico = np.random.gamma(8, 2)
            if not self.es_recambio:
                self.tiempo_resolucion = np.random.normal(45, 6)
            else:
                self.tiempo_resolucion = np.random.normal(120, 14)

    def definir_horas(self):
        #self.dia_llamada, self.hora_salida_callcenter = addMin(self.hora_entrada_callcenter, self.tiempo_callcenter)
        #self.dia_llamada, self.hora_atencion = addMin(self.hora_salida_callcenter, self.tiempo_atencion)
        #self.dia_llamada, self.hora_diagnostico = addMin(self.hora_atencion, self.tiempo_diagnostico)
        #self.dia_llamada, self.hora_resolucion = addMin(self.hora_diagnostico, self.tiempo_resolucion)
        pass

    def minutos_totales(self):
        minutos_totales = int(self.minuto_inicial)
        if self.dia_llamada == 'martes':
            minutos_totales += 1440
        elif self.dia_llamada == 'miercoles':
            minutos_totales += 2880
        elif self.dia_llamada == 'jueves':
            minutos_totales += 4320
        elif self.dia_llamada == 'viernes':
            minutos_totales += 5760
        self.minutos = minutos_totales
        self.minuto_inicial = minutos_totales

    def minutos_totales_procesados(self):
        minutos_totales = int(self.hora_salida_callcenter)
        if self.dia_llamada == 'martes':
            minutos_totales += 1440
        elif self.dia_llamada == 'miercoles':
            minutos_totales += 2880
        elif self.dia_llamada == 'jueves':
            minutos_totales += 4320
        elif self.dia_llamada == 'viernes':
            minutos_totales += 5760
        self.minutos = minutos_totales

    def __str__(self):
        return f'''Falla:
                  comuna: {self.comuna}
                  dia: {self.dia_llamada}
                  hora inicio: {self.hora_llamada}
                  tiempo call center: {self.tiempo_callcenter}
                  hora salida call center: {self.hora_salida_callcenter}
                  tiempo diagnostico: {self.tiempo_diagnostico}
                  tiempo resolucion: {self.tiempo_resolucion}'''

    def __repr__(self):
        return self.__str__()