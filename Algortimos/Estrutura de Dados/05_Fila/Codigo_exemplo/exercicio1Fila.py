# Dada uma fila de inteiros, escreva um
# progrma queexclua todos os números inteiros
# negativos e mostre a fila no final

from queue import Queue

fila1 = Queue()
fila2 = Queue()

for i in range(10, -11, -2):
    print(i, end=" ")
    fila1.enqueue(i)

print()

while not fila1.is_empty():
    valor = fila1.dequeue()
    if valor >= 0:
        fila2.enqueue(valor)
        print(valor, end=" ")
