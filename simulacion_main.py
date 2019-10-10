from Clase_Falla import Falla
from generador_llamadas import parametros
from Clase_Utilitario import instanciar_tecnicos, disponibilidad_tecnicos
from tiempos_sin_nulos import getTime, matriz_fuera_punta, matriz_punta
from parametros import horario_punta_final
from simulacion_servidores import Simulacion, simulacion_remota
from operadores import instanciar_operadores, disponibilidad_operadores
import math
import csv


def cumple_promesas(lista_de_fallas):
    promesas_incumplidas = 0
    tiempo_incumplimiento = 0
    l_promesas = []
    hora_y_media = 0
    for falla in lista_de_fallas:
        momento = math.ceil(
            falla.hora_entrada_callcenter / 720)  # indica si estamos en una mañana(impar) o una tarde (par)
        momento_res = math.ceil(falla.tiempo_total / 720)

        if falla.hora_atencion - falla.hora_entrada_callcenter > 240:
            promesas_incumplidas += 1
            tiempo_incumplimiento += falla.hora_atencion - falla.hora_entrada_callcenter
            l_promesas.append(falla)

        elif momento_res > momento + 1:
            promesas_incumplidas += 1
            # tiempo_incumplimiento += falla.hora_atencion - falla.hora_entrada_callcenter
            tiempo_incumplimiento += falla.tiempo_total - (momento + 1) * 720
            l_promesas.append(falla)

        if falla.hora_atencion - falla.hora_entrada_callcenter < 91:
            hora_y_media += 1

    if promesas_incumplidas == 0:
        porcentaje_incumplimiento = 0
        promedio_incumplimiento = 0
    else:
        porcentaje_incumplimiento = promesas_incumplidas / len(lista_de_fallas)
        promedio_incumplimiento = tiempo_incumplimiento / promesas_incumplidas

    return promesas_incumplidas, tiempo_incumplimiento, l_promesas, porcentaje_incumplimiento, \
           promedio_incumplimiento, hora_y_media


def sortear_por_minutos(elem):
    return elem[0].minutos


def sortear_por_tiempo_total(elem):
    return elem.tiempo_total


def simulacion():
    n = 0
    busquedas_kit = 0
    eventos_terminados = []
    eventos_sabado = 0
    minutos_utilitarios_desperdiciados = 0

    while n <= 3:

        # n es el número de semanas que se simularán

        '''event_line = [(Falla(comuna='san joaquin', dia_llamada='lunes', hora_llamada=520), 'contestar_llamada'), (Falla(comuna='san joaquin', dia_llamada='lunes', hora_llamada=520), 'contestar_llamada'),
                      (Falla(comuna='san joaquin', dia_llamada='lunes', hora_llamada=520), 'contestar_llamada')]
        for evento in event_line:
            evento[0].hora_entrada_callcenter = 520  # OJO: no siempre entraría al call center al mi
            evento[0].tiempo_callcenter = 240  # tiempo que pasa en callcenter
            evento[0].hora_salida_callcenter = 520 + 240  # hora de salida de callcenter
            evento[0].hora_atencion = None  # hora en que llega a la casa
            evento[0].tiempo_atencion = None  # tiempo que demora desde que le dan el llamado hasta  llegar a la casa
            evento[0].hora_diagnostico = None  # hora en que termina de diagnosticar la falla
            evento[0].tiempo_diagnostico = 240  # tiempo que se demora en diagnosticar la falla
            evento[0].hora_resolucion = None  # hora en que termina el llamado'''

        event_line = []
        # lugar donde están los eventos
        current_time = 0
        # tiempo actual que se usa para guardar los cambios de estado de los eventos
        tecnicos = instanciar_tecnicos()
        # se llama a la cantidad de tecnicos necesarios y se especifica su horario (ver archivo utilitario)
        operadores = instanciar_operadores()
        # lo mismo que los tecnicos, pero para operarios del callcenter (ver archivo operadores)

        for dia in parametros.keys():
            for comuna in parametros[dia].keys():
                for llamada in parametros[dia][comuna]['llamados']:
                    event_line.append((Falla(comuna, dia, llamada), 'contestar_llamada'))
        # se generan las llamadas con el archivo generar llamadas, y se crean las fallas con esos datos.
        # en el event_line es una lista de tuplas, con el primer elemento la falla en sí y el segundo qué es la
        # próxima acción a realizar, se actualiza cada vez

        '''#event_line.sort(key=sortear_por_minutos)
        sim = Simulacion(5, event_line)
        event_line = sim.run()'''

        # event_line = simulacion_remota[n]

        '''for falla in event_line:
            if falla[1] == 'asignar_tecnico':
                falla[0].minutos_totales_procesados()
            else:
                falla[0].minutos_totales()'''

        event_line.sort(key=sortear_por_minutos)
        # se ordena la lista por cuál evento es el más proximo a pasar

        '''for element in event_line:
            print(element[0])'''

        m = 0
        # se usa el m para ver en que punto de la lista estamos parados, cosa de que si no se puede completar el proximo
        # evento a realizar, ya sea por falta de operarios o tecnicos, se mire el siguiente evento.

        while current_time < 7200:

            # print(f'Tiempo actual: {current_time}')

            '''for element in event_line:
                print(element[1])'''

            for tecnico in tecnicos:
                if (current_time not in tecnico.hora_turno) and not tecnico.ocupado:
                    tecnico.ubicacion = 'san joaquin'
                    tecnico.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
                if (current_time in tecnico.hora_turno) and not tecnico.ocupado:
                    minutos_utilitarios_desperdiciados += 1

            if not event_line:
                print('Se acabaron los clientes de la semana')
                # si no hay mas eventos, no hay mas que hacer.
                current_time = 100000
                break

            elif event_line[m][1] == 'contestar_llamada':
                # print('Llegó un llamado al callcenter.')
                if disponibilidad_operadores(operadores, current_time):
                    # se chequea si hay algun operador desocupado que este de turno
                    # print('Se contestó llamado.')
                    # print(len(event_line))
                    for operador in operadores:
                        if not operador.ocupado and (current_time in operador.hora_turno):
                            if current_time < int(event_line[m][0].minutos):
                                current_time = int(event_line[m][0].minutos)
                            # se le asigna una falla al operador desocupado.
                            operador.falla = event_line[m][0].id
                            operador.ocupado = True
                            nuevo_evento = event_line[m][0]
                            event_line.pop(m)
                            m = 0
                            nuevo_evento.hora_entrada_callcenter = current_time
                            nuevo_evento.hora_salida_callcenter = current_time + int(nuevo_evento.tiempo_callcenter)
                            nuevo_evento.minutos = current_time + int(nuevo_evento.tiempo_callcenter)
                            event_line.append((nuevo_evento, 'terminar_llamada'))
                            # se vuelve a agregar el evento actualizado a la linea de eventos y se vuelve a ordenar.
                            event_line.sort(key=sortear_por_minutos)
                            break
                else:
                    # print('No hay operarios disponibles en este momento.')
                    m += 1

            elif event_line[m][1] == 'terminar_llamada':
                # se desocupa el operario que esta relacionado a la falla en la que se termina la llamada.
                # print('Se terminó un llamado del callcenter.')
                if current_time < int(event_line[m][0].minutos):
                    current_time = int(event_line[m][0].minutos)
                for operador in operadores:
                    if operador.falla == event_line[m][0].id:
                        operador.ocupado = False
                        operador.falla = None
                        break
                nuevo_evento = event_line[m][0]
                event_line.pop(m)
                m = 0
                event_line.append((nuevo_evento, 'asignar_tecnico'))
                # se asigna la nueva accion al evento.
                event_line.sort(key=sortear_por_minutos)

            elif event_line[m][1] == 'asignar_tecnico':
                tecnicos_actuales = []
                # a continuacion se verifica cuantps tecnicos son necesarios, de ser necesarios dos se elimina de la
                # lista de utilitarios disponibles a todos los que solo tengan un tecnico.
                if event_line[m][0].grupo == 'A' or event_line[m][0].grupo == 'C':
                    # print('se necesitan dos tecnicos')
                    for tecnico in tecnicos:
                        if tecnico.cantidad_tecnicos == 2:
                            # print('Se agrego tecnico')
                            tecnicos_actuales.append(tecnico)
                else:
                    tecnicos_actuales = tecnicos
                    # print('No se necesitan dos tecnicos')
                # se revisa que de la lista resultante haya algun tecnico disponible.
                if disponibilidad_tecnicos(tecnicos_actuales, current_time):
                    if current_time < int(event_line[m][0].minutos):
                        current_time = int(event_line[m][0].minutos)
                    # print('Técnico asignado.')
                    for tecnico in tecnicos_actuales:
                        if not tecnico.ocupado and (current_time in tecnico.hora_turno):
                            for tecnico2 in tecnicos:
                                if tecnico2.id == tecnico.id:
                                    tecnico2.falla = event_line[m][0].id
                                    tecnico2.ocupado = True
                                    tecnico2.hora_asignacion = current_time
                                    # print(f'Tecnico {tecnico2.id} ocupado. Tiempo actual: {current_time}.')
                                    nuevo_evento = event_line[m][0]
                                    event_line.pop(m)
                                    m = 0
                                    # se revisa si es necesario ir a la central a buscar repuestos por las fallas.
                                    # despues se ve el tiempo de llegada hasta el lugar al que van a ir.
                                    # el tiempo en el que se terminara el proximo evento de la falla esta guardado en
                                    # su atributo minutos. Se guarda su proxima ubicacion para futuros calculos.
                                    if nuevo_evento.grupo == 'A':
                                        if tecnico2.repuestos[1] == 0 or tecnico2.repuestos[4] == 0 or \
                                                tecnico2.repuestos[8] == 0:
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
                                            nuevo_evento.minutos = current_time + int(
                                                getTime(matriz_punta, tecnico2.ubicacion,
                                                        'santiago'))
                                        else:
                                            nuevo_evento.minutos = current_time + int(
                                                getTime(matriz_fuera_punta, tecnico2.ubicacion,
                                                        'santiago'))
                                    else:
                                        if current_time in horario_punta_final:
                                            nuevo_evento.minutos = current_time + int(
                                                getTime(matriz_punta, tecnico2.ubicacion,
                                                        nuevo_evento.comuna))
                                        else:
                                            nuevo_evento.minutos = current_time + int(
                                                getTime(matriz_fuera_punta, tecnico2.ubicacion,
                                                        nuevo_evento.comuna))
                                    event_line.append((nuevo_evento, evento))
                                    event_line.sort(key=sortear_por_minutos)
                                    break
                            break
                    '''tecnicos_ocupados = []
                    for tecnico in tecnicos:
                        if tecnico.ocupado:
                            tecnicos_ocupados.append(tecnico.falla)
                    print(tecnicos_ocupados)
                    print(len(tecnicos_ocupados))'''
                else:
                    # si no hay tecnicos disponibles se trabaja en el siguiente evento.
                    m += 1

            elif event_line[m][1] == 'ir_central':
                # print('Técnico llego a central.')
                busquedas_kit += 1
                for tecnico in tecnicos:
                    if event_line[m][0].id == tecnico.falla:
                        # se restablece el numero de kits del tecnico
                        tecnico.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
                        tecnico.ubicacion = 'santiago'
                        break
                if current_time < int(event_line[m][0].minutos):
                    current_time = int(event_line[m][0].minutos)
                nuevo_evento = event_line[m][0]
                event_line.pop(m)
                m = 0
                for tecnico in tecnicos:
                    if nuevo_evento.id == tecnico.falla:
                        # se calcula el nuevo tiempo de desplazamiento para llegar a terreno.
                        if current_time in horario_punta_final:
                            nuevo_evento.minutos = current_time + int(getTime(matriz_punta, tecnico.ubicacion,
                                                                              nuevo_evento.comuna))
                        else:
                            nuevo_evento.minutos = current_time + int(getTime(matriz_fuera_punta, tecnico.ubicacion,
                                                                              nuevo_evento.comuna))
                        break
                event_line.append((nuevo_evento, 'llegar_terreno'))
                event_line.sort(key=sortear_por_minutos)

            elif event_line[m][1] == 'llegar_terreno':
                # print('Técnico llegó a terreno.')
                if current_time < int(event_line[m][0].minutos):
                    current_time = int(event_line[m][0].minutos)
                nuevo_evento = event_line[m][0]
                nuevo_evento.hora_atencion = current_time
                for tecnico in tecnicos:
                    if event_line[m][0].id == tecnico.falla:
                        tecnico.ubicacion = event_line[m][0].comuna
                        break
                event_line.pop(m)
                m = 0
                # se acutaliza el tiempo de cuando se terminara el evento y se le vuelve a agregar a la linea de eventos
                nuevo_evento.minutos = current_time + int(nuevo_evento.tiempo_diagnostico)
                event_line.append((nuevo_evento, 'terminar_diagnostico'))
                event_line.sort(key=sortear_por_minutos)

            elif event_line[m][1] == 'terminar_diagnostico':
                # print('Se termina diagnóstico.')
                if current_time < int(event_line[m][0].minutos):
                    current_time = int(event_line[m][0].minutos)
                nuevo_evento = event_line[m][0]
                event_line.pop(m)
                m = 0
                # se actualizan los tiempos de terminos para proximo evento de la falla.
                nuevo_evento.minutos = current_time + int(nuevo_evento.tiempo_resolucion)
                event_line.append((nuevo_evento, 'realizar_reparacion'))
                event_line.sort(key=sortear_por_minutos)

            elif event_line[m][1] == 'realizar_reparacion':
                # print('Se realiza reparación.')
                if current_time < int(event_line[m][0].minutos):
                    current_time = int(event_line[m][0].minutos)
                for tecnico in tecnicos:
                    if event_line[m][0].id == tecnico.falla:
                        if event_line[m][0].es_recambio:
                            # si es recambio se le descuenta un repuesto.
                            tecnico.repuestos[event_line[m][0].tipo] -= 1
                        if current_time not in tecnico.hora_turno and current_time not in horario_punta_final:
                            # si termina el trabajo y se acaba su turno tiene que volver a la central.
                            # es cuando horario no es punta
                            event_line[m][0].tiempo_total = int(current_time - event_line[m][0].hora_entrada_callcenter)
                            tecnico.ubicacion = 'san joaquin'
                            tecnico.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
                        elif current_time not in tecnico.hora_turno and current_time in horario_punta_final:
                            # si termina el trabajo y se acaba su turno tiene que volver a la central.
                            # es para hora
                            event_line[m][0].tiempo_total = int(current_time - event_line[m][0].hora_entrada_callcenter)
                            tecnico.ubicacion = 'san joaquin'
                            tecnico.repuestos = {1: 2, 2: 1, 3: 1, 4: 6, 5: 5, 6: 1, 7: 2, 8: 1}
                        else:
                            # si todavia esta de turno no se mueve para ningun lado.
                            # tengo que revisar esto denuevo, porque tecnicos solo vuelven a central cuando terminan
                            # trabajo.
                            event_line[m][0].tiempo_total = int(current_time - event_line[m][0].hora_entrada_callcenter)
                        tecnico.ocupado = False
                        # print(f'Técnico {tecnico.id} desocupado. Tiempo actual: {current_time}.')
                        tecnico.falla = None
                        break
                eventos_terminados.append(event_line[m][0])
                event_line.pop(m)
                event_line.sort(key=sortear_por_minutos)
                m = 0

        eventos_sabado += len(event_line)
        # cantidad de eventos dejados para el sabado
        # print(len(eventos_terminados))
        n += 1

    eventos_terminados.sort(key=sortear_por_tiempo_total)

    for element in eventos_terminados:
        print(element)

    tiempo_desperdiciado_dia = (((minutos_utilitarios_desperdiciados / 4) / 5) / 60) / len(tecnicos)

    print('\n############RESULTADOS FINALES############\n')

    print(f'Se dejaron {eventos_sabado} eventos para el sábado.')
    print(f'Se completaron {len(eventos_terminados)} eventos.')
    print(n)
    tuplas_datos = cumple_promesas(eventos_terminados)
    print(f'Promesas incumplidas: {tuplas_datos[0]}')
    print(f'Tiempo total incumplimiento: {tuplas_datos[1]}')
    # print(f'Tiempo total incumplimiento: {tuplas_datos[2]}')
    print(f'Porcentaje incumplimiento: {tuplas_datos[3]}')
    print(f'Promedio incumplimiento: {tuplas_datos[4]}')
    print(f'Número de idas a buscar kits: {busquedas_kit}')
    print(f'Minutos de utilitarios desprediciados: {minutos_utilitarios_desperdiciados}')
    print(f'Horas perdidas por día por utilitario: {tiempo_desperdiciado_dia}')
    print(f'Diagnóstica antes de la hora y media: {tuplas_datos[5]}')

    resultados_finales = [len(eventos_terminados), eventos_sabado, tuplas_datos[0], tuplas_datos[1], tuplas_datos[3],
                          tuplas_datos[4]]
    resultados_texto = f'Prueba,{len(eventos_terminados)},{eventos_sabado},{tuplas_datos[0]},{tuplas_datos[1]},' \
                       f'{tuplas_datos[3]},{tuplas_datos[4]},{tuplas_datos[5]},{minutos_utilitarios_desperdiciados},' \
                       f'{tiempo_desperdiciado_dia}\n'
    # print(resultados_finales)

    with open('resultados.csv', 'a') as fd:
        fd.write(resultados_texto)


for i in range(60):
    simulacion()
