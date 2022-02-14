#!/usr/bin/env python
# coding: utf-8

# ## Construa um programa que mostre se o número inserido no sistema é par ou ímpar;


numero_digitado = int(input('Digite o número desejado '))
print(f'O número digitado foi: {numero_digitado}')


# Descrevendo se o número digitado é par ou ímpar

if numero_digitado % 2 == 0:
    print(f'O número {numero_digitado} é par')
else:
    print(f'O número {numero_digitado} é ímpar')

