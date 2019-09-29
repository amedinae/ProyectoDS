import json
import ds
import numpy as np

data = []
with open('10680.json') as a:
    data.append(json.load(a)) # Dinámica

with open('16809.json') as b:
    data.append(json.load(b)) # Digital

with open('18473.json') as c:
    data.append(json.load(c)) # Señales 2

with open('21949.json') as d:
    data.append(json.load(d)) # Intensive

with open('22969.json') as e:
    data.append(json.load(e)) # Gráfica interactiva

# for i in range(data[1]['count']):
#     print(data[1]['list'][i]['week'])
#     for j in range(len(data[1]['list'][i]['week'])):
#         for h in range(len(data[1]['list'][i]['week'][j])):
#             print(data[1]['list'][i]['week'][j][h])

listaGrupos = []
for k in range(len(data)):
    grupo = ds.Queue()
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
                            ultimaHora = 10*int(data[k]['list'][i]['week'][j][h][3]) + int(data[k]['list'][i]['week'][j][h][4])

                    # print("primeraHora {}".format(primeraHora))
                    # print("ultimaHora {}".format(ultimaHora))

                    for x in range(primeraHora - 6, ultimaHora - 6, 1):
                        zeors_array[x][j] = 1
        grupo.enqueue({'matriz': zeors_array, 'grupo': i, 'asignatura': k})
        # print(zeors_array)
        # print('-------------------------------')
    listaGrupos.append(grupo)

print(listaGrupos)






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

# def potencia(c):
#     if len(c) == 0:
#         return [[]]
#     r = potencia(c[:-1])
#     return r + [s + [c[-1]] for s in r]
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

