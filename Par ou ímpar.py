#!/usr/bin/env python
# coding: utf-8

# ## Construa um programa que mostre se o número inserido no sistema é par ou ímpar; E se ele é divisível por qual número (2, 3, 4, 5, 6, 7, 8, 9, 10 ou 12)

# In[22]:


numero_digitado = int(input('Digite o número desejado '))
print(f'O número digitado foi: {numero_digitado}')


# In[23]:


# Descreve se o número digitado é par ou ímpar

if numero_digitado % 2 == 0:
    print(f'O número {numero_digitado} é par')
else:
    print(f'O número {numero_digitado} é ímpar')

