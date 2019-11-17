import json
from AvlTree import AvlTree

arbol = AvlTree()
with open('10680.json') as a:
    data = json.load(a)  # Dinámica
root = None
for i in range(10):
    with open('Datos falsos/{}.json'.format(i), 'w') as f:
        root = arbol.insert(t=root, key=[i, json.dump(data, f)])
arbol.preOrder(root)