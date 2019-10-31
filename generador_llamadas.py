import numpy as np
import scipy.stats as ss
from parametros import params, horas
import copy

'''
Estructura : params :{
    dia: {comuna: {lambdas: [], repeticiones:[], llamados:[])}}
'''


def get_llamado(franja: list):
    '''
    Función que recibe una lista con los límites de cada
    franja probabilística, y retorna la cantidad total
    de llamados que hubo en base a esas probabilidades
    '''
    r = np.random.uniform(0, 1)
    # print(f'--EL NUMERO ES {r}')
    for i in range(21):
        if r > franja[20-i]:
            return 20-i
    return 0


def crear_listas(params: dict):
    for dia, dicc1 in params.items():
        for comuna, dicc2 in dicc1.items():
            for lmbda in dicc2["lambdas"]:
                franja = [0]
                for i in range(21):
                    # Construyo las probabilidades
                    franja.append(franja[-1]+ss.poisson.pmf(i, lmbda))
                franja.pop(0)
                index = get_llamado(franja)
                dicc2["repeticiones"].append(index)
            # print(dicc2["repeticiones"])


def asignar_horas(params: dict, horas: list):
    for dia, dicc1 in params.items():
        for comuna, dicc2 in dicc1.items():
            for repeticion_franja in range(len(dicc2["repeticiones"])):
                for i in range(dicc2["repeticiones"][repeticion_franja]):
                    r = np.random.uniform(
                        horas[repeticion_franja][0],
                        horas[repeticion_franja][1])
                    minuto = r*60
                    dicc2["llamados"].append(minuto)
                        #minutos_a_horas(minuto))
                    # print(minutos_a_horas(minuto))
                dicc2["llamados"].sort()
            #print(f'LLAMADOS DIA {dia}, {comuna}: {dicc2["llamados"]}')
        #print('\n\n')


def minutos_a_horas(minutos: int):
    return f"{str(minutos//60).zfill(2)}:{str(minutos%60).zfill(2)}"


def generar_llamados(params, horas):
    output = copy.deepcopy(params)
    crear_listas(output)
    asignar_horas(output, horas)
    return output



# AQUI HAGO UNA COPIA DEL DICCIONARIO, CON DEEPCOPY NO SE COPIAN
# REFERENCIAS, POR LO QUE SOLO SE MODIFICA OUTPUT. "PARAMS" QUEDA 
# TAL CUAL ESTA INSTANCIADO.
'''
output = generar_llamados(params, horas)
print(output)
print(params)

'''