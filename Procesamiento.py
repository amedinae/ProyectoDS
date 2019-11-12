from BinaryHeap import BinaryHeap
import json
import numpy as np


def horarioVacio():
    horario = [0 for x in range(112)]
    return horario


def setHoras(curso, dia, primeraHora, ultimaHora):
    for y in range(dia * 16 + primeraHora - 6, dia * 16 + ultimaHora - 6):
        curso[y] = 1
    return curso



data = []
with open('10680.json') as a:
    data.append(json.load(a))  # Dinámica

with open('16809.json') as b:
    data.append(json.load(b))  # Digital

with open('18473.json') as c:
    data.append(json.load(c))  # Señales 2

with open('21949.json') as d:
    data.append(json.load(d))  # Intensive

with open('22969.json') as e:
    data.append(json.load(e))  # Gráfica interactiva

data[0].update({"materia": "DINAMICA", "C_M": 5, "C_G": [1, 2, 3, 4]})
data[1].update({"materia": "DIGITAL", "C_M": 4, "C_G": [1, 2, 3, 4, 5, 6, 7, 8]})
data[2].update({"materia": "SEÑALES II", "C_M": 3, "C_G": [x for x in range(data[2]['count'])]})
data[3].update({"materia": "INTENSIVE", "C_M": 2, "C_G": [x for x in range(data[3]['count'])]})
data[4].update({"materia": "GRAFICA INTERACTIVA", "C_M": 1, "C_G": [x for x in range(data[4]['count'])]})
# with open('16706.json', encoding='utf-8') as q:
# 	data.append(json.load(q))

# with open('16707.json', encoding='utf-8') as g:
# 	data.append(json.load(g))

# with open('16809.json') as h:
# 	data.append(json.load(h))
primeraHora = 0
ultimaHora = 0

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
        grupo.append({'horario': horario, 'grupo': i, 'asignatura': data[k]['materia'], 'C_M': data[k]['C_M'],
                      'C_G': data[k]['C_G'][i]})
    listaGrupos.append(grupo)

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
    resultado = [{'horario': horarioVacio(), 'grupo': [], 'asignatura': [], 'C_H': 0} for x in range(len(listas))]
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
        if sirve:
            horarios.insert(resultado[i]['C_H'], {'asignaturas': resultado[i]['asignatura'], 'grupos': resultado[i]['grupo']})
    return horarios.H

# print(data)
# print(combinatoria(listaGrupos)[1])
# printHorario(sumarListas(combinatoria(listaGrupos))[0]['horario'])
# print(sumarListas(combinatoria(listaGrupos))[0]['horario'])
print(sumarListas(combinatoria(listaGrupos)))
# algo = sumarListas(combinatoria(listaGrupos))
# with open('data.json', 'w') as f:
#     json.dump(algo,f)
# print(listaGrupos[0][1]['horario'])
# print(listaGrupos)