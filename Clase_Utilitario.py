class Utilitario:
    def __init__(self, ubicacion_inicial, hora_turno, cantidad_tecnicos):
        self.cantidad_tecnicos = cantidad_tecnicos
        self.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
        self.hora_inicio_turno = hora_turno
        self.hora_fin_turno = None
        self.ubicacion = ubicacion_inicial

    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion