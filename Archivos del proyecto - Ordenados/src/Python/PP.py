from BinaryHeap import BinaryHeap
from ds import QueueList
import json
import numpy as np


def horarioVacio():
    horario = [0 for x in range(112)]
    return horario


def setHoras(curso, dia, primeraHora, ultimaHora):
    for y in range(dia * 16 + primeraHora - 6, dia * 16 + ultimaHora - 6):
        curso[y] = 1
    return curso


def leerMaterias():
    with open('calificados.json') as a:
        data = json.load(a)  # Dinámica
    return data


def organizarHorario(data):
    # primeraHora = 0
    # ultimaHora = 0

    listaGrupos = []
    for k in range(len(data)):
        grupo = []
        for i in range(data[k]['count']):
            horario = horarioVacio()
            primeraHora = 0
            ultimaHora = 0
            for j in range(7):
                for h in range(len(data[k]['list'][i]['week'][j])):
                    a = data[k]['list'][i]['week'][j][h][0]
                    if a != '-':
                        if int(a) > 5:
                            if int(data[k]['list'][i]['week'][j][h][2]) > 1:
                                primeraHora = int(a)
                                ultimaHora = int(data[k]['list'][i]['week'][j][h][2])
                            else:
                                primeraHora = int(a)
                                ultimaHora = 10 + int(data[k]['list'][i]['week'][j][h][3])
                        elif int(a) == 1:
                            if int(data[k]['list'][i]['week'][j][h][3]) > 5:
                                primeraHora = 10 + int(data[k]['list'][i]['week'][j][h][1])
                                ultimaHora = int(data[k]['list'][i]['week'][j][h][3])
                            else:
                                primeraHora = 10 + int(data[k]['list'][i]['week'][j][h][1])
                                ultimaHora = 10 * int(data[k]['list'][i]['week'][j][h][3]) + int(
                                    data[k]['list'][i]['week'][j][h][4])
                        horario = setHoras(horario, j, primeraHora, ultimaHora)
            grupo.append({'horario': horario, 'grupo': i, 'asignatura': data[k]['materia'], 'codigo': data[k]['code'], 'C_M': data[k]['C_M'],
                          'C_G': data[k]['C_G'][i]})
        listaGrupos.append(grupo)

    return listaGrupos

# data[0]['list'] --------------------------------------------------------- lista de cursos ----------------------------
# data[0]['list'][1]['code'] --------------------------------------------------- GRUPO ---------------------------------
# data[0]['list'][1]['master'] ------------------------------------------------ PROFESOR -------------------------------
# data[0]['list'][1]['free'] ------------------------------------------------ CUPOS LIBRES -----------------------------
# data[0]['list'][1]['quota'] ----------------------------------------------- CUPOS TOTALES ----------------------------
# data[0]['list'][1]['week'] ---------------------------------------------- HORARIO [arreglo] --------------------------


# *******************Combina los diferentes grupos de horarios sin sumarlos ********************************************

def combinatoria(lista):
    c = np.zeros(len(lista))
    tamano = []
    for l in range(len(lista)):
        tamano.append(len(lista[l]))

    total = []
    while tamano[0] > c[0]:
        salida = []
        for x in range(len(lista)):
            salida.append(lista[x][int(c[x])])
        c[len(lista) - 1] += 1
        total.append(salida)
        for j in reversed(range(len(lista))):
            if c[j] == tamano[j] and j - 1 >= 0:
                c[j - 1] += 1
                c[j] = 0
                if c[0] == tamano[0]:
                    return total
            else:
                break
    return total


# listas[i][j]['grupo'] -------------------------- Toma el número del grupo de una asignatura --------------------------
# listas[i][j]['asignatura'] --------------------- Toma el nombre de una asignatura ------------------------------------

def sumarListas(listas):
    resultado = [{'horario': horarioVacio(), 'grupo': [], 'codigo': [], 'asignatura': [], 'C_H': 0} for x in range(len(listas))]
    horarios = BinaryHeap(len(listas))

    for i in range(len(resultado)):
        sirve = True
        for j in range(len(listas[i])):
            resultado[i]['C_H'] += listas[i][j]['C_G']*listas[i][j]['C_M']

            for z in range(len(resultado[i]['horario'])):
                if resultado[i]['horario'][z] + listas[i][j]['horario'][z] < 2:
                    resultado[i]['horario'][z] += listas[i][j]['horario'][z]
                else:
                    sirve = False
                    break
            if not sirve:
                break
            resultado[i]['grupo'].append(listas[i][j]['grupo'])
            resultado[i]['asignatura'].append(listas[i][j]['asignatura'])
            resultado[i]['codigo'].append(listas[i][j]['codigo'])
        if sirve:
            horarios.insert(resultado[i]['C_H'], {'asignaturas': resultado[i]['asignatura'], 'codigos': resultado[i]['codigo'], 'grupos': resultado[i]['grupo']})
    return horarios


def prioridadHorario(horarios, k):
    cola = QueueList()
    for i in range(k):
        cola.enqueue(horarios.extractMax())
    return cola

# def registroUsuarios():


if __name__ == '__main__':
    algo = sumarListas(combinatoria(organizarHorario(leerMaterias())))
    print("Bienvenido al visualizador de Poderak")
    print("¿Cuántos horarios quieres visualizar?")
    n = int(input())
    cola_ordenada = prioridadHorario(algo, n)
    cola_final = []
    for x in range(n):
        cola_final.append(cola_ordenada.dequeue()) #Conversión a objeto serializable, para que se pueda transformar en un JSON
    print(cola_final)
    #with open('C:/Users/juand/Desktop/Horario/Ordenar/data/data.json', 'w') as f:
        #json.dump(cola_final, f)