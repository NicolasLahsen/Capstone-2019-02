class Operador:

    class_counter = 0

    def __init__(self, tipo_operador):
        self.__tipo_operador = tipo_operador
        self.hora_turno = self.generador_horas()
        self.__ocupado = False
        self.id = Operador.class_counter
        self.__falla = None
        Operador.class_counter += 1

    @property
    def tipo_operador(self):
        return self.__tipo_operador

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

    def generador_horas(self):
        minutos_permitidos = []
        if self.tipo_operador == 1:
            # turno de las 7 a las 19
            for i in range(420, 1140):
                minutos_permitidos.append(i)
            for i in range(1860, 2580):
                minutos_permitidos.append(i)
            for i in range(3300, 4020):
                minutos_permitidos.append(i)
            for i in range(4740, 5460):
                minutos_permitidos.append(i)
            for i in range(6180, 6900):
                minutos_permitidos.append(i)
        else:
            # turno de las 19 a las 7
            for i in range(420):
                minutos_permitidos.append(i)
            for i in range(1140, 1860):
                minutos_permitidos.append(i)
            for i in range(2580, 3300):
                minutos_permitidos.append(i)
            for i in range(4020, 4740):
                minutos_permitidos.append(i)
            for i in range(5460, 6180):
                minutos_permitidos.append(i)
            for i in range(6900, 7201):
                minutos_permitidos.append(i)
        return minutos_permitidos


def instanciar_operadores():
    lista = []
    for i in range(5):
        lista.append(Operador(1))
    for i in range(1):
        lista.append(Operador(2))
    return lista


def disponibilidad_operadores(lista, current_time):
    for operador in lista:
        if not operador.ocupado and (int(current_time) in operador.hora_turno):
            # si encuentra un tecnico disponible retorna verdadero, que esté en turno
            return True
    return False
