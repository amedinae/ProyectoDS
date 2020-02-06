import json
from AvlTree import AvlTree

arbol = AvlTree()
with open('10680.json') as a:
    data = json.load(a)  # Dinámica
root = None
for i in range(1000000):
    root = arbol.insert(t=root, key=[i, data])
arbol.preOrder(root)



