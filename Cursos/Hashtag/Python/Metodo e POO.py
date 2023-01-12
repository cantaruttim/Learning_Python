""""
Tudo no Python é um objeto. Portanto pensamos numa classe
Portanto, apresentam Métodos específicos da classe

classe Pessoa:

métodos:      Atributos
- Andar   :    10km
- Pular   :    1,5m
- Comer   :    1Kg de comida por dia
- Aprender :   Python

Vamos criar nossas próprias Classes
E nossos próprios métodos
Ex. class Stack

"""
# a=[1,2,3,4,5]
#nome= 'Matheus'

#print(type(nome.capitalize())) # <class 'str'>
# print(type(a)) # <class 'list'>


######################################################################################

#Obs¹ Polimorfismo classe + subclasses

class TV:
    def __init__(self, tamanho):
        self.cor = 'preta'
        self.canal = 'Netflix'
        self.Ligado = False
        self.tamanho = tamanho
        self.volume = 10

    def mudar_canal(self, novo_canal): #novo_parametro
        self.canal = novo_canal
        print(f'Canal alterado para o canal {novo_canal}')



tv_sala = TV(tamanho=55)
tv_quarto = TV(tamanho=70)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)
