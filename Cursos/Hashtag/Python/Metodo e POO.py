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

    def __init__(self):
        self.cor = 'preta'
        self.canal = 'Netflix'
        self.Ligado = False
        self.tamanho = 55
        self.volume = 10

tv_sala = TV()
tv_quarto = TV()

print(tv_sala.cor())

