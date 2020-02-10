from BinaryHeap import BinaryHeap
from ds import QueueList
import json
import numpy as np

def hash(key):
    return sum([ord(c) for c in key])%37    

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
            lista_borrable = [0 for x in range(37)]
            lista_borrable[hash('horario')] = horario
            lista_borrable[hash('grupo')] = i
            lista_borrable[hash('asignatura')] = data[k]['materia']
            lista_borrable[hash('codigo')] = data[k]['code']
            lista_borrable[hash('C__m')] = data[k]['C_M']
            lista_borrable[hash('C_G')] = data[k]['C_G'][i]
            grupo.append(lista_borrable)
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
    resultado = []
    for x in range(len(listas)):
        lista_borrable = [0 for a in range(37)]
        lista_borrable[hash('horario')] = horarioVacio()
        lista_borrable[hash('grupo')] = []
        lista_borrable[hash('codigo')] = []
        lista_borrable[hash('asignatura')] = []
        lista_borrable[hash('C_H')] = 0
        resultado.append(lista_borrable)
    horarios = BinaryHeap(len(listas))
    for i in range(len(resultado)):
        sirve = True
        for j in range(len(listas[i])):
            resultado[i][hash('C_H')] += listas[i][j][hash('C_G')]*listas[i][j][hash('C__m')]
            for z in range(len(resultado[i][hash('horario')])):
                if resultado[i][hash('horario')][z] + listas[i][j][hash('horario')][z] < 2:
                    resultado[i][hash('horario')][z] += listas[i][j][hash('horario')][z]
                else:
                    sirve = False
                    break
            if not sirve:
                break
            resultado[i][hash('grupo')].append(listas[i][j][hash('grupo')])
            resultado[i][hash('asignatura')].append(listas[i][j][hash('asignatura')])
            resultado[i][hash('codigo')].append(listas[i][j][hash('codigo')])
        if sirve:
            l = [0 for a in range(37)]
            l[hash('asignaturas')] = resultado[i][hash('asignatura')]
            l[hash('codigos')] = resultado[i][hash('codigo')]
            l[hash('grupos')] =  resultado[i][hash('grupo')]
            horarios.insert(resultado[i][hash('C_H')],l)
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
    print(2)
    cola_ordenada = prioridadHorario(algo, n)
    cola_final = []
    for x in range(n):
        cola_final.append(cola_ordenada.dequeue()) #Conversión a objeto serializable, para que se pueda transformar en un JSON
    print(cola_final)
    #with open('C:/Users/juand/Desktop/Horario/Ordenar/data/data.json', 'w') as f:
        #json.dump(cola_final, f)

