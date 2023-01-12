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
"""
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
"""

#################################################################################

# Sistema de Banco
from datetime import datetime
import pytz # faz ajuste de fuso-horário


class ContaCorrente:
    @staticmethod # nao usa nada da classe. Método Estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR


    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0 # iniciando o saldo com zero
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    # criando os métodos que representam a conta : consultar saldo, sacar e depositar dinheiro na conta
    # Recomenda-se realizar qualquer ação de uma classe por um atributo da classe
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(valor, self.saldo, ContaCorrente._data_hora())


    def _limite_conta(self):
        self.limite = -1000 # definindo o valor de limite
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo() # podemos chamar uma função de um atributo diferente
        else:
            self.saldo -= valor
            self.transacoes.append(-valor, self.saldo, ContaCorrente._data_hora())


# PROGRAMA
conta = ContaCorrente('Matheus', '123.456.789 - 11', 1234, 34062)
conta.consultar_saldo() # utilizando o método para consultar saldo

conta.depositar(5000)
conta.consultar_saldo()

conta.sacar(2000)
conta.consultar_saldo()

conta.sacar(3500)
conta.consultar_saldo()

conta.depositar(4780)
