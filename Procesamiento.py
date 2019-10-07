import json
import ds
import numpy as np


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
        c[len(lista)-1] += 1
        total.append(salida)
        for j in reversed(range(len(lista))):
            if c[j] == tamano[j] and j-1 >= 0:
                c[j-1] += 1
                c[j] = 0
                if c[0] == tamano[0]:
                    return total
            else:
                break
    return total

def sumarListas(listas):
    horarios = ds.Queue()
    for i in range(len(listas)):
        resultado = {'matriz': np.zeros((16, 7)), 'grupo': [], 'asignatura': []}
        sirve = True
        for j in range(len(listas[i])):
            resultado['matriz'] += listas[i][j]['matriz']
            resultado['grupo'].append(listas[i][j]['grupo'])
            resultado['asignatura'].append(listas[i][j]['asignatura'])
            for x in range(16):
                for y in range(7):
                    if resultado['matriz'][x][y] > 1:
                        sirve = False
        if sirve:
            horarios.enqueue(resultado)
    return horarios

# def sumarListas(listas):
#     horarios = []
#     for i in range(len(listas)):
#         resultado = {'matriz': np.zeros((16, 7)).tolist(), 'grupo': [], 'asignatura': []}
#         sirve = True
#         for j in range(len(listas[i])):
#             resultado['matriz'] += listas[i][j]['matriz'].tolist()
#             resultado['grupo'].append(listas[i][j]['grupo'])
#             resultado['asignatura'].append(listas[i][j]['asignatura'])
#             for x in range(16):
#                 for y in range(7):
#                     if resultado['matriz'][x][y] > 1:
#                         sirve = False
#         if sirve:
#             horarios.append(resultado)
#     return horarios


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


listaGrupos = []
for k in range(len(data)):
    grupo = []
    for i in range(data[k]['count']):
        zeors_array = np.zeros((16, 7))
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

                    for x in range(primeraHora - 6, ultimaHora - 6, 1):
                        zeors_array[x][j] = 1
        grupo.append({'matriz': zeors_array, 'grupo': i, 'asignatura': k})
    listaGrupos.append(grupo)

# print(listaGrupos)

# print(sumarListas(combinatoria(listaGrupos)))
print(sumarListas(combinatoria(listaGrupos)).size)


# for r in range(len(combinatoria(listaGrupos))):
#     for t in range(len(data)):
#         final = data[algo.dequeue()['asignatura']]
