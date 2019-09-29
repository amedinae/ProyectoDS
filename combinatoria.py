import ds

n = int(input("Por favor ingrese el número de productos \n"))
while True:
    productos = input("Ahora ingrese los productos \n")
    array_in = [str(i) for i in productos.split()]
    if(len(array_in)!=n):
        print("Ingrese {} productos".format(n))
    else:
        break

m = int(input("Por favor ingrese el número de tiendas \n"))
while True:
    tamanoEnvio = input("Ahora por favor ingrese la cantidad de productos que corresponden a cada tienda en su respectivo orden \n")
    array_in_m = [int(i) for i in tamanoEnvio.split()]
    if(len(array_in_m)!=m):
        print("Ingrese {} números que indiquen la cantidad de productos a cada tienda".format(m))
    else:
        break

pilaProductos = ds.Stack()
colaTiendas = ds.Queue()
for j in reversed(array_in):
    pilaProductos.push(j)
    
current = ds.Stack()
contador = 1
for x in array_in_m:
    for y in range(x):
        current.push(pilaProductos.pop())
    colaTiendas.enqueue(current)
    print("Pila {} \n {} \n".format(contador,current))
    contador = contador + 1
    current = ds.Stack()
print("Cola \n {} \n".format(colaTiendas))
