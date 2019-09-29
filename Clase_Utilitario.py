class Utilitario:
    def __init__(self, ubicacion_inicial, cantidad_tecnicos, tipo_turno):
        self.cantidad_tecnicos = cantidad_tecnicos
        self.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
        self.ubicacion = ubicacion_inicial
        self.tipo_turno = tipo_turno
        self.hora_turno = self.generador_horas()

    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    def generador_horas(self):
        minutos_permitidos = []
        if self.tipo_turno == '1':
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
        elif self.tipo_turno == '2':
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
