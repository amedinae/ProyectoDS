import ds
import json
import numpy as np

def horarioVacio():
	horario = [0 for x in range(112)]
	return horario

def setHoras(curso,dia,primeraHora,ultimaHora):
	for y in range(dia*16+primeraHora-6,dia*16+ultimaHora-6):
		curso[y]=1
	return curso

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

with open('16706.json') as f:
	data.append(json.load(f))

with open('16707.json') as g:
	data.append(json.load(g))

with open('16809.json') as h:
	data.append(json.load(h))
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
							ultimaHora = 10*int(data[k]['list'][i]['week'][j][h][3]) + int(data[k]['list'][i]['week'][j][h][4])
					horario = setHoras(horario,j,primeraHora,ultimaHora)
		grupo.append({'horario':horario, 'grupo': i, 'asignatura': k})
	listaGrupos.append(grupo)

# def sumarLists(listas):
# 	resultado = [0 for x in range(len(listas[0]))]
# 	for i in range(len(resultado)):	
# 		for lista in listas:
# 				resultado[i] += lista[i]		
# 	return resultado

#print(sumarListas([[1,2],[2,1],[3,4]]))
#print([sum(x) for x in zip([1,2,4],[2,1,4],[3,4,4])])

def sacarLista(listas):
	combinacion = []
	combinaciones =[]
	for x in listas:
		for y in x:
			combinacion.append(y['horario'])
		combinaciones.append(combinacion)
		combinacion = []
	print(combinaciones)

def sumarListas(listas):
	resultado = [{'horario': horarioVacio() , 'grupo': [], 'asignatura': []} for x in range(len(listas))]
	horarios = ds.Queue()
	
	for i in range(len(resultado)):
		sirve = True
		for j in range(len(listas[i])):	
			for z in range(len(resultado[i]['horario'])): 
				resultado[i]['horario'][z] += listas[i][j]['horario'][z]
			resultado[i]['grupo'].append(listas[i][j]['grupo'])
			resultado[i]['asignatura'].append(listas[i][j]['asignatura'])
			for x in range(112):
				if (resultado[i]['horario'][x] > 1):
					sirve = False
		if sirve:
			horarios.enqueue(resultado[i])			
	return horarios

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
			if c[j] == tamano[j] and j-1 >=0:
				c[j-1] += 1
				c[j] = 0
				if c[0] == tamano[0]:
					return total
			else:
				break
	return total


def printHorario(horario):
	for y in range(7):
		s = ""
		for x in range(y,16*7,16):
			s += str(horario[x])
		print(s)

#printHorario(sumarListas(combinatoria(listaGrupos))[0]['horario'])
#print(sumarListas(combinatoria(listaGrupos))[0]['horario'])
print(sumarListas(combinatoria(listaGrupos)))
# algo = sumarListas(combinatoria(listaGrupos))
# with open('data.json', 'w') as f:
    #json.dump(algo, f)
#print(listaGrupos[0][1]['horario'])
#print(listaGrupos)


			