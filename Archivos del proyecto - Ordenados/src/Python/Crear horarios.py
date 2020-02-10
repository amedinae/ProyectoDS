import json
from AvlTree import AvlTree

arbol = AvlTree()
with open('C:/Users/diego/OneDrive/Escritorio/Andres Felipe/Nueva carpeta (2)/ProyectoDS/10680.json') as a:
    data = json.load(a)  # Dinámica
root = None
for i in range(1000000):
    root = arbol.insert(t=root, key=data)
arbol.preOrder(root)



