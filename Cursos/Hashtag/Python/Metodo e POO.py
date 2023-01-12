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

    """
    Criar um objeto ContaCorrente para gerenciar as contas dos clinetes

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do cliente
        agencia (int): Número da agência responsável
        num_conta (int): Número da conta do cliente
        saldo (int): Saldo disponível na conta do cliente

    """



    @staticmethod # nao usa nada da classe. Método Estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0 # iniciando o saldo com zero
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    # criando os métodos que representam a conta : consultar saldo, sacar e depositar dinheiro na conta
    # Recomenda-se realizar qualquer ação de uma classe por um atributo da classe
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))


    def _limite_conta(self):
        self._limite = -1000 # definindo o valor de limite
        return self._limite

    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo() # podemos chamar uma função de um atributo diferente
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))


    def consultar_historico(self):
        print("Histórico de Transações")
        print("Valor, Saldo, Data e Hora")
        for transacao in self._transacoes:
            print(transacao)


    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))








# PROGRAMA
conta = ContaCorrente('Matheus', '123.456.789 - 11', 1234, 34062)
conta.consultar_saldo() # utilizando o método para consultar saldo

conta.depositar(5000)
conta.consultar_saldo()

print('-' * 20)
conta_gabs = ContaCorrente('Gbariella', '123.958.554 - 11', 4321, 78554)
conta.transferir(1500, conta_gabs)

conta.consultar_saldo()
conta_gabs.consultar_saldo()
conta.consultar_historico()
conta_gabs.consultar_historico()


# help(ContaCorrente) podemos dar um help na nossa classe e ele exibe a DocString da classe