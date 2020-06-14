from BinaryHeap import BinaryHeap

horarios = BinaryHeap(1000000)

for x in range(1000000):
	horarios.insert(x,x)

for x in range(1000000):
	horarios.extractMax()