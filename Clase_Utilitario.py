class Utilitario:

    class_counter = 0

    def __init__(self, ubicacion_inicial, cantidad_tecnicos, tipo_turno):
        self.cantidad_tecnicos = cantidad_tecnicos
        self.__repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
        self.__ubicacion = ubicacion_inicial
        self.tipo_turno = tipo_turno
        self.hora_turno = self.generador_horas()
        self.__ocupado = False
        self.id = Utilitario.class_counter
        self.__falla = None
        self.__tiempo_trabajo = 0
        self.__tiempo_termino = 0
        self.lista_fallas = list()
        self.horarios_comienzo = self.generador_comienzos()
        Utilitario.class_counter += 1

    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, statement):
        self.__ocupado = statement

    @property
    def falla(self):
        return self.__falla

    @falla.setter
    def falla(self, fallas):
        self.__falla = fallas

    @property
    def repuestos(self):
        return self.__repuestos

    @repuestos.setter
    def repuestos(self, diccionario):
        self.__repuestos = diccionario

    @property
    def tiempo_trabajo(self):
        return self.__tiempo_trabajo

    @tiempo_trabajo.setter
    def tiempo_trabajo(self, inicio):
        self.__tiempo_trabajo = inicio

    @property
    def tiempo_termino(self):
        return self.__tiempo_termino

    @tiempo_termino.setter
    def tiempo_termino(self, termino):
        self.__tiempo_termino = termino

    def generador_horas(self):
        minutos_permitidos = []
        if self.tipo_turno == 3:
            # turno de las 20 a las 6
            for i in range(360):
                minutos_permitidos.append(i)
            for i in range(1200, 1800):
                minutos_permitidos.append(i)
            for i in range(2640, 3240):
                minutos_permitidos.append(i)
            for i in range(4080, 4680):
                minutos_permitidos.append(i)
            for i in range(5520, 6120):
                minutos_permitidos.append(i)
            for i in range(6960, 7201):
                minutos_permitidos.append(i)
        elif self.tipo_turno == 1:
            # turno de las 6 a las 16
            for i in range(360, 960):
                minutos_permitidos.append(i)
            for i in range(1800, 2400):
                minutos_permitidos.append(i)
            for i in range(3240, 3840):
                minutos_permitidos.append(i)
            for i in range(4680, 5280):
                minutos_permitidos.append(i)
            for i in range(6120, 6720):
                minutos_permitidos.append(i)
        else:
            # turno de las 12 a las 20
            for i in range(720, 1200):
                minutos_permitidos.append(i)
            for i in range(2160, 2640):
                minutos_permitidos.append(i)
            for i in range(3600, 4080):
                minutos_permitidos.append(i)
            for i in range(5040, 5520):
                minutos_permitidos.append(i)
            for i in range(6480, 6960):
                minutos_permitidos.append(i)
        return minutos_permitidos

    def generador_comienzos(self):
        horarios = []
        if self.tipo_turno == 3:
            # turno de las 20 a las 6
            horarios.append(0)
            horarios.append(1200)
            horarios.append(2640)
            horarios.append(4080)
            horarios.append(5520)
            horarios.append(6960)

        elif self.tipo_turno == 1:
            # turno de las 6 a las 16
            horarios.append(360)
            horarios.append(1800)
            horarios.append(3240)
            horarios.append(4680)
            horarios.append(6120)

        else:
            # turno de las 12 a las 20
            horarios.append(720)
            horarios.append(2160)
            horarios.append(3600)
            horarios.append(5040)
            horarios.append(6480)

        return horarios


def instanciar_tecnicos():
    lista = []
    for i in range(1):
        lista.append(Utilitario('las condes', 1, 1))
        lista.append(Utilitario('penalolen', 1, 1))
        lista.append(Utilitario('santiago', 1, 2))
        lista.append(Utilitario('penalolen', 1, 2))
        lista.append(Utilitario('las condes', 1, 3))
        lista.append(Utilitario('santiago', 1, 3))
        lista.append(Utilitario('penalolen', 1, 3))
        lista.append(Utilitario('las condes', 2, 3))
        lista.append(Utilitario('santiago', 2, 3))
        lista.append(Utilitario('penalolen', 2, 3))
    for i in range(2):
        lista.append(Utilitario('santiago', 1, 1))
        lista.append(Utilitario('las condes', 2, 1))
        lista.append(Utilitario('santiago', 2, 1))
        lista.append(Utilitario('las condes', 1, 2))
        lista.append(Utilitario('las condes', 2, 2))
        lista.append(Utilitario('santiago', 2, 2))
    for i in range(3):
        lista.append(Utilitario('penalolen', 2, 1))
        lista.append(Utilitario('penalolen', 2, 2))
    '''for i in range(4):
        lista.append(Utilitario('san joaquin', 1, 1))
        lista.append(Utilitario('san joaquin', 1, 2))
    for i in range(7):
        lista.append(Utilitario('san joaquin', 2, 1))
        lista.append(Utilitario('san joaquin', 2, 2))
    for i in range(3):
        lista.append(Utilitario('san joaquin', 1, 3))
    for i in range(3):
        lista.append(Utilitario('san joaquin', 2, 3))'''
    return lista


def disponibilidad_tecnicos(lista, current_time):
    for tecnico in lista:
        if not tecnico.ocupado and (int(current_time) in tecnico.hora_turno):
            # si encuentra un tecnico disponible retorna verdadero, que esté en turno
            return True
    return False

