## Teste para prova de programação de quinta feira

#1 Crie um programa que determine a quatidade de consoantes de uma palavra

def quantidadeConso(frase):
    consoantes = 'bcdfghjklmnpqrstvxzwBCDFGHJKLMNPQRSTVXZW'
    cont = 0 
    
    for letra in frase:
        if letra in consoantes:
            cont = cont + 1 ## prestar atenção para a indentação
    return cont

quantidadeConso("Gosto")

#2 Crie um programa que determine a quantidade de vogais

def quantidadeVogais(frase):
    vogais = 'aeiouAEIOU'
    cont = 0 
    
    for letra in frase:
        if letra in vogais:
            cont = cont + 1
    return cont

quantidadeVogais("Mimoso")

#3 Determine a quantidade total de dias transcrridos do vetor até um indice expecífico (representado
#  pelo mês vigente em sequência)

def quantidadeTotal(dia, mes):
    vet = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    soma = 0 
    
    for i in range(mes - 1): #aqui consideramos que o mês vigente ainda não passou.
        """
        aqui nós especificamos o mês que queremos, por exemplo, julho
        e após adicionarmos o dia, verificamos que os dias passados até o dia 20 de julho
        contamos todos os dias (representado pelo vetor até o mês de junho)
        e somamos os dias passados do mês de julho (de 1 até o dia 20)   
        
        """
        soma = soma + vet[i]
    return soma + dia

quantidadeTotal(20, 7)

#4 some os valores de um vetor

vet2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

soma = 0 
for i in range(len(vet2)): ## range de valores 
    """
    
    Neste exercício quis somar todos os valores de um vetor
    Sem expecificar um índice específico. Porem caso queira somar os valores de um indicie específico
    A lógica seria a do mesmo exercício anterior. 
    Teríamos que especificar dois valores -- fazendo uma função 
    
    def somatoria(x, y):
    
    """
    soma = soma + vet2[i]
    
print(soma)

#5 some os valores pares do vet3

vet3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cont = 0 
for i in range(len(vet3)):
    if i % 2 == 0:
        cont = cont + vet3[i]

print(cont)

## Estudos com NUMPY

import numpy as np

def borda(dimensao):
  mat = np.zeros( (dimensao, dimensao), dtype=np.int32 )
  for l in range(len(mat)):
    for c in range(len(mat[0])):
      if l==0 or c==0 or l==len(mat)-1 or c==len(mat[0])-1:
        mat[l][c] = 1

  print(np.matrix(mat))


A = np.zeros((2, 2), dtype=np.float32)
print(A)

# crie um Array 

a = np.array([1, 2, 3, 4, 5, 6,])
b = np.array([[1, 2, 3, 4, 5, 6,], [2, 3, 4, 5, 6, 7]])

print(a) # matriz unidmimensional

# matriz multidimensional (N-DIMENSIONAL ARRAY)
print(b[0]) # mostra a primeira linha da matriz
print(b[1]) # mostra a segunda linha da matriz

c = np.empty(3)
print(c)

d = np.zeros(3)
e = np.ones(3)

print(d, e)

## criando um array com um range de valores

f = np.arange(5) ## [0 1 2 3 4 5] lembre-se o indice inicia com 0
print(f)


# podemos concatenar arraies de mesmo tamanho axis = 0 (linhas)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
g = np.concatenate((x, y), axis=0)

print(g)
