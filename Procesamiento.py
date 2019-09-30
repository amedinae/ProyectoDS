import json
import ds
import numpy as np
import itertools

# def potencia(c):
#     if len(c) == 0:
#         return [[]]
#     r = potencia(c[:-1])
#     return r + [s + [c[-1]] for s in r]
#
#
# def combinaciones(c, n):
#     return [s for s in potencia(c) if len(s) == n]

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
        # print(c[1])
        c[len(lista)-1] += 1
        total.append(salida)
        # print(c[len(lista)-1])
        for j in reversed(range(len(lista))):
            if c[j] == tamano[j] and j-1 >=0:
                # print(c[1])
                c[j-1] += 1
                c[j] = 0
                if c[0] == tamano[0]:
                    return total
            else:
                break
    return total

def sumarListas(listas):
    resultado = [{'matriz': np.zeros((16, 7)) , 'grupo': [], 'asignatura': []} for x in range(len(listas))]
    for i in range(len(resultado)):
        for j in range(len(listas[i])):
            resultado[i]['matriz'] += listas[i][j]['matriz']
            resultado[i]['grupo'].append(listas[i][j]['grupo'])
            resultado[i]['asignatura'].append(listas[i][j]['asignatura'])
    return resultado

# def sumarListas(listas):
#     resultado = [0 for x in range(len(listas[0]))]
#     for i in range(len(resultado)):
#         for lista in listas:
#             resultado[i] += lista[i]
#     return resultado

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

# for i in range(data[1]['count']):
#     print(data[1]['list'][i]['week'])
#     for j in range(len(data[1]['list'][i]['week'])):
#         for h in range(len(data[1]['list'][i]['week'][j])):
#             print(data[1]['list'][i]['week'][j][h])

listaGrupos = []
for k in range(len(data)):
    grupo = []
    for i in range(data[k]['count']):
        zeors_array = np.zeros((16, 7))
        primeraHora = 0
        ultimaHora = 0
        for j in range(7):
            for h in range(len(data[k]['list'][i]['week'][j])):
                # for k in range(len(data[0]['list'][i]['week'][j][0])):
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

                    # print("primeraHora {}".format(primeraHora))
                    # print("ultimaHora {}".format(ultimaHora))

                    for x in range(primeraHora - 6, ultimaHora - 6, 1):
                        zeors_array[x][j] = 1
        grupo.append({'matriz': zeors_array, 'grupo': i, 'asignatura': k})
        # print(zeors_array)
        # print('-------------------------------')
    listaGrupos.append(grupo)

# print(listaGrupos)
algo = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
#print(sumarListas(combinatoria(listaGrupos)))
print(sumarListas(combinatoria(listaGrupos))[0]['matriz'])
# print(combinatoria(listaGrupos))
# print(sumarListas([[0, 1, 0], [1, 0, 1], [0, 1, 0]]))

# print(sum([[1, 2, 3, 4, 5], [1, 1, 1, 1, 1]]))
# prueba = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10]]
# for r in itertools.product([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10]],[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10], [6, 7, 8, 9, 10]]):
#     print(str(r[0]) + str(r[1]) )
#
#
# for v in range(len(data)):
#     suma = []
#     # for w in range(data[v]['count']):
#     a = listaGrupos[v].dequeue().data['matriz']
#     suma.append(a)
#     print(suma)
#
# def sumatoria(matriz):


# def sumar_matrices(matriz, contador):
#     if len(matriz) - 1 == contador:
#         return 0
#     sumatoria


#
# print(potencia([1,2,3]))

# for v in range(data[0]['count']):
#
#     for w in range(data[1]['count']):
#
#         for x in range(data[2]['count']):
#
#             for y in range(data[3]['count']):
#
#                 for z in range(data[4]['count']):
