from Clase_Falla import Falla, addMin
from generador_llamadas import parametros


def sortear_por_minutos(elem):
    return elem[0].minutos


n = 0
promesas_incumplidas = 0
tiempo_incumplimiento = 0
trabajos_incumplidos = 0

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

    m = 0

    '''while current_time <= 7200:

        if event_line[m][1] == 'contestar_llamada':
            pass

        elif event_line[m][1] == 'terminar_llamada':
            pass

        elif event_line[m][1] == 'asignar_tecnico':
            pass

        elif event_line[m][1] == 'ir_central':
            pass

        elif event_line[m][1] == 'llegar_terreno':
            pass

        elif event_line[m][1] == 'terminar_diagnostico':
            pass

        elif event_line[m][1] == 'realizar_ajuste':
            pass

        elif event_line[m][1] == 'realizar_recambio':
            pass'''

    n += 1
