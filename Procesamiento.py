import json
import ds
import numpy as np

data = []
with open('10680.json') as a:
    data.append(json.load(a)) # Dinámica

with open('16809.json') as b:
    data.append(json.load(b)) # Digital

with open('18473.json') as c:
    data.append(json.load(c))

with open('21949.json') as d:
    data.append(json.load(d))

with open('22969.json') as e:
    data.append(json.load(e))

zeors_array = np.zeros((16, 7))
primeraHora = 0
ultimaHora = 0

# for i in range(data[0]['count']):
#     print(data[0]['list'][i]['week'])

for i in range(data[0]['count']):
    for j in range(7):
        # for k in range(len(data[0]['list'][i]['week'][j][0])):
        a = data[0]['list'][i]['week'][j][0][0]
        if a != '-':
            if int(a) > 1:
                if int(data[0]['list'][i]['week'][j][0][2]) > 1:
                    primeraHora = int(a)
                    ultimaHora = int(data[0]['list'][i]['week'][j][0][2])
                else:
                    primeraHora = int(a)
                    ultimaHora = 10 + int(data[0]['list'][i]['week'][j][0][3])
            elif int(a) == 1:
                if int(data[0]['list'][i]['week'][j][0][3]) > 1:
                    primeraHora = 10 + int(data[0]['list'][i]['week'][j][0][1])
                    ultimaHora = int(data[0]['list'][i]['week'][j][0][3])
                else:
                    primeraHora = 10 + int(data[0]['list'][i]['week'][j][0][1])
                    ultimaHora = 10 + int(data[0]['list'][i]['week'][j][0][4])

            # print("primeraHora {}".format(primeraHora))
            # print("ultimaHora {}".format(ultimaHora))

            for x in range(primeraHora-6, ultimaHora-5, 1):
                zeors_array[x][j] = 1
print(zeors_array)


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

print(potencia([1,2,3]))

# for v in range(data[0]['count']):
#
#     for w in range(data[1]['count']):
#
#         for x in range(data[2]['count']):
#
#             for y in range(data[3]['count']):
#
#                 for z in range(data[4]['count']):

