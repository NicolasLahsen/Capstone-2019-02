from Clase_Falla import Falla
from generador_llamadas import parametros
from Clase_Utilitario import instanciar_tecnicos, disponibilidad_tecnicos
from tiempos_sin_nulos import getTime, matriz_fuera_punta, matriz_punta
from parametros import horario_punta_final


def sortear_por_minutos(elem):
    return elem[0].minutos


n = 0
promesas_incumplidas = 0
tiempo_incumplimiento = 0
trabajos_incumplidos = 0
eventos_terminados = []
eventos_sabado = 0

while n <= 4:

    event_line = [(Falla('vitacura', 'lunes', '08:40'), 'asignar_tecnico'), (Falla('providencia', 'martes', '00:15'), 'asignar_tecnico'),
                  (Falla('santiago', 'jueves', '12:00'), 'asignar_tecnico')]
    current_time = 0
    tecnicos = instanciar_tecnicos()

    '''for dia in parametros.keys():
        for comuna in parametros[dia].keys():
            for llamada in parametros[dia][comuna]['llamados']:
                event_line.append((Falla(comuna, dia, llamada), 'contestar_llamada'))'''

    event_line.sort(key=sortear_por_minutos)

    for element in event_line:
        print(element[0])

    m = 0

    while current_time < 7200:

        print(f'Tiempo actual: {current_time}')

        for element in event_line:
            print(element[1])

        if not event_line:
            print('Se acabaron los clientes de la semana')
            current_time = 100000
            break

        elif event_line[m][1] == 'contestar_llamada':
            pass

        elif event_line[m][1] == 'terminar_llamada':
            pass

        elif event_line[m][1] == 'asignar_tecnico':
            tecnicos_actuales = []
            if event_line[m][0].personal == 2:
                print('se necesitan dos tecnicos')
                for tecnico in tecnicos:
                    if tecnico.cantidad_tecnicos == 2:
                        print('Se agrego tecnico')
                        tecnicos_actuales.append(tecnico)
            else:
                tecnicos_actuales = tecnicos
                print('No se necesitan dos tecnicos')
            if disponibilidad_tecnicos(tecnicos_actuales, current_time):
                current_time = int(event_line[m][0].minutos)

                for tecnico in tecnicos_actuales:
                    if not tecnico.ocupado:
                        for tecnico2 in tecnicos:
                            if tecnico2.id == tecnico.id:
                                tecnico2.falla = event_line[m][0].id
                                tecnico2.ocupado = True
                                nuevo_evento = event_line[m][0]
                                event_line.pop(m)
                                m = 0
                                if nuevo_evento.grupo == 'A':
                                    if tecnico2.repuestos[1] == 0 or tecnico2.repuestos[4] == 0 or tecnico2.repuestos[8] == 0:
                                        evento = 'ir_central'
                                    else:
                                        evento = 'llegar_terreno'
                                elif nuevo_evento.grupo == 'B':
                                    if tecnico2.repuestos[3] == 0 or tecnico2.repuestos[5] == 0 or \
                                            tecnico2.repuestos[7] == 0:
                                        evento = 'ir_central'
                                    else:
                                        evento = 'llegar_terreno'
                                else:
                                    if tecnico2.repuestos[2] == 0 or tecnico2.repuestos[6] == 0:
                                        evento = 'ir_central'
                                    else:
                                        evento = 'llegar_terreno'
                                if evento == 'ir_central':
                                    if current_time in horario_punta_final:
                                        nuevo_evento.minutos += int(getTime(matriz_punta, tecnico2.ubicacion, 'santiago'))
                                    else:
                                        nuevo_evento.minutos += int(getTime(matriz_fuera_punta, tecnico2.ubicacion,
                                                                        'santiago'))
                                else:
                                    if current_time in horario_punta_final:
                                        nuevo_evento.minutos += int(getTime(matriz_punta, tecnico2.ubicacion,
                                                                        nuevo_evento.comuna))
                                    else:
                                        nuevo_evento.minutos += int(getTime(matriz_fuera_punta, tecnico2.ubicacion,
                                                                        nuevo_evento.comuna))
                                event_line.append((nuevo_evento, evento))
                                event_line.sort(key=sortear_por_minutos)
                                break
                        break
            else:
                m += 1

        elif event_line[m][1] == 'ir_central':
            for tecnico in tecnicos:
                if event_line[m][0].id == tecnico.falla:
                    tecnico.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
                    tecnico.ubicacion = 'santiago'
                    break
            current_time = int(event_line[m][0].minutos)
            nuevo_evento = event_line[m][0]
            event_line.pop(m)
            m = 0
            for tecnico in tecnicos:
                if nuevo_evento.id == tecnico.falla:
                    if current_time in horario_punta_final:
                        nuevo_evento.minutos += int(getTime(matriz_punta, tecnico.ubicacion,
                                                        nuevo_evento.comuna))
                    else:
                        nuevo_evento.minutos += int(getTime(matriz_fuera_punta, tecnico.ubicacion,
                                                        nuevo_evento.comuna))
                    break
            event_line.append((nuevo_evento, 'llegar_terreno'))
            event_line.sort(key=sortear_por_minutos)

        elif event_line[m][1] == 'llegar_terreno':
            print('Se llego al terreno')
            current_time = int(event_line[m][0].minutos)
            nuevo_evento = event_line[m][0]
            for tecnico in tecnicos:
                if event_line[m][0].id == tecnico.falla:
                    tecnico.ubicacion = event_line[m][0].comuna
                    break
            event_line.pop(m)
            m = 0
            nuevo_evento.minutos += int(nuevo_evento.tiempo_diagnostico)
            event_line.append((nuevo_evento, 'terminar_diagnostico'))
            event_line.sort(key=sortear_por_minutos)

        elif event_line[m][1] == 'terminar_diagnostico':
            print('se termina diagnostico')
            current_time = int(event_line[m][0].minutos)
            nuevo_evento = event_line[m][0]
            event_line.pop(m)
            m = 0
            nuevo_evento.minutos += int(nuevo_evento.tiempo_resolucion)
            event_line.append((nuevo_evento, 'realizar_reparacion'))
            event_line.sort(key=sortear_por_minutos)

        elif event_line[m][1] == 'realizar_reparacion':
            print('se realiza reparacion')
            current_time = int(event_line[m][0].minutos)
            for tecnico in tecnicos:
                if event_line[m][0].id == tecnico.falla:
                    if current_time not in tecnico.hora_turno and current_time not in horario_punta_final:
                        event_line[m][0].tiempo_total = int(current_time + getTime(matriz_fuera_punta,
                                                                               event_line[m][0].comuna, 'san joaquin') \
                                                        - event_line[m][0].minuto_inicial)
                        tecnico.ubicacion = 'san joaquin'
                    elif current_time not in tecnico.hora_turno and current_time in horario_punta_final:
                        event_line[m][0].tiempo_total = int(current_time + getTime(matriz_punta,
                                                                               event_line[m][0].comuna, 'san joaquin')\
                                                        - event_line[m][0].minuto_inicial)
                        tecnico.ubicacion = 'san joaquin'
                    else:
                        event_line[m][0].tiempo_total = int(current_time - event_line[m][0].minuto_inicial)
                    tecnico.ocupado = False
                    tecnico.falla = None
                    break
            eventos_terminados.append(event_line[m][0])
            event_line.pop(m)
            event_line.sort(key=sortear_por_minutos)
            m = 0

    eventos_sabado += len(event_line)
    n += 1

print('\n############RESULTADOS FINALES############\n')

print(f'Se dejaron {eventos_sabado} eventos para el sábado.')
print(f'Se completaron {eventos_terminados} eventos.')

#for evento in eventos_terminados:

