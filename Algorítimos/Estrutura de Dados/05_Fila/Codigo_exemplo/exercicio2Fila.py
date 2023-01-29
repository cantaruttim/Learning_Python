# Escreva um programa que
# inverta o conteúdo de uma fila
from queue import Queue
from Stack import Stack

fila1 = Queue()
pilha = Stack()

for i in range(10, -11, -2):
    print(i, end=" ")
    fila1.enqueue(i)

print()
print("Colocando na pilha:")
while not fila1.is_empty():
    valor = fila1.dequeue()
    pilha.push(valor)
    print(valor, end=" ")

print()
print("Colocando na fila:")
while not pilha.is_empty():
    valor = pilha.pop()
    fila1.enqueue(valor)
    print(valor, end=" ")
