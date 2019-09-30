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


listaGrupos = []
for k in range(len(data)):
    grupo = ds.Queue()
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
                            ultimaHora = 10*int(data[k]['list'][i]['week'][j][h][3]) + int(data[k]['list'][i]['week'][j][h][4])

                    for x in range(primeraHora - 6, ultimaHora - 6, 1):
                        zeors_array[x][j] = 1
        grupo.enqueue({'matriz': zeors_array, 'grupo': i, 'asignatura': k})
    listaGrupos.append(grupo)

print(listaGrupos)