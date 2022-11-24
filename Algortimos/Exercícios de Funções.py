#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números     


# In[1]:


def numPar():
    numPar_lista = []
    
    for i in range(1,21):
        
        if i % 2 == 0:
            numPar_lista.append(i)
            print(numPar_lista)
    return numPar

numPar()


# In[ ]:


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string


# In[2]:


def textoMaiusculo():
    text = input('digite o texto que vc quer converter')
    return text.upper()

textoMaiusculo()


# In[ ]:


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista


# In[3]:


def lista():
    lista_elementos = ['banana', 'maçã', 'laranja', 'melão']
    
    for i in range(0,2):
        novo = input('você tem direito a adicionar dois novos elementos a lista: ')
        lista_elementos.append(novo)
    
    return lista_elementos

lista() 
    


# In[ ]:


# Exercício 4 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles


# In[4]:


def soma(numx, numy): return numx+numy

soma(10, 1585)


# In[5]:


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)

Explicação:

as variáveis globais são variáveis que existem fora da função. Ou seja, seus valores não irão interferir nos resultados obtidos dentro de qualquer operação realizada pela função.

Já os valores atribuidos à soma, são responsáveis por gerar um resultado que só existe dentro da função. Portanto, ao chamar a função soma, com os valores 10 e 20, obteremos a soma de ambos os números (ou o valor atribuido a uma determinada operação atribuida a eles)