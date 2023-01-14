
"""
A função cria_conta, determina os parâmetros necessários para criar uma conta

atributos:
    numero (str) : mostra o número da conta
    titular (str : mostra o nome do titular da conta
    saldo (float) : mostra o saldo positivo ou negativo da conta do titular
    limite (float) : determina o limite da conta

"""

def cria_conta(numero, titular, saldo, limite):
    conta = {"número": numero, "titular": titular, "saldo": saldo, "limite":limite}
    return conta


"""
A função deposita, realiza a operação de depósito;

atributos:
    conta (int) : determina o número da conta
    valor (float) : determina o valor a ser depositado na conta

"""


def deposita(conta, valor):
    conta['saldo'] += valor


"""
A função saca, realiza a operação de saque;

atributos:
    conta (int) : determina o número da conta
    valor (float) : determina o valor a ser depositado na conta

"""

def saca(conta, valor):
    conta['saldo'] -= valor


"""
A função extrato mostra o valor atual da conta;

atributos:
    conta (int) : determina o número da conta
    

"""

def extrato(conta):
    print(f"número {conta['número']} \nsaldo : {conta['saldo']}")



conta = cria_conta('123-4', 'Matheus', 120.0, 1000.0)
deposita(conta, 500)
extrato(conta)

