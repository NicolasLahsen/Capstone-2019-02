from Clase_Falla import Falla, addMin
from generador_llamadas import parametros


def sortear_por_minutos(elem):
    return elem[0].minutos


n = 0

while n <= 4:

    event_line = []
    current_time = 0

    for dia in parametros.keys():
        for comuna in parametros[dia].keys():
            for llamada in parametros[dia][comuna]['llamados']:
                event_line.append((Falla(comuna, dia, llamada), 'contestar_llamada'))

    event_line.sort(key=sortear_por_minutos)

    for element in event_line:
        print(element[0])

    while current_time <= 7200:



    n += 1
