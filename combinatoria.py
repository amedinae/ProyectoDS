import ds
import json

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

def sumarListas(listas):
	resultado = [0 for x in range(len(listas[0]))]
	for i in range(len(resultado)):	
		for lista in listas:
				resultado[i] += lista[i]		
	return resultado
	

#print(listaGrupos[0][1]['horario'])
#print(listaGrupos)


			