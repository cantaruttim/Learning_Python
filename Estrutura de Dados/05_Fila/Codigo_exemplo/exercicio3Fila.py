from queue import Queue
from Stack import Stack


pilha = Stack()
fila1 = Queue()
fila2 = Queue()

for i in range(10,-2, -1):
    print(i, end=" ")
    fila1.enqueue(i)

print()

for i in range(1,10):
    print(i, end=" ")
    fila2.enqueue(i)

print()

while not fila1.is_empty() or not fila2.is_empty():
    if not fila1.is_empty():
        valor = fila1.dequeue()
        if valor % 2 == 0:
            print("Empilhando - da fila1: ", valor)
            pilha.push(valor)
        else:
            if not pilha.is_empty():
                valor = pilha.pop()
                print("Desempilhando - da fila1: ", valor)
            else:
                print("Pilha vazia.")
    else:
        print("Fila 1 esta vazia.")

    if not fila2.is_empty():
        valor = fila2.dequeue()
        if valor % 2 == 0:
            print("Empilhando - da fila2: ", valor)
            pilha.push(valor)
        else:
            if not pilha.is_empty():
                valor = pilha.pop()
                print("Desempilhando - da fila2: ", valor)
            else:
                print("Pilha vazia.")
    else:
        print("Fila 2 esta vazia.")