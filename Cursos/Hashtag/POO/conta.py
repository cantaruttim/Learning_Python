import datetime

class Conta:

    """
    Quando uma classe é criada, todos os seus atributos é inicializado
    pelo método __init__(); O método __new__() que roda por trás do interpretador Python
    é quem é o método construtor.

    O método __new__() que é chamado pelo método inicializador, devolve uma instância do objeto
    e em seguida.

    Ao	 criar	uma	Conta, estamos pedindo para o Python criar uma nova instância de Conta na
    memória, ou	 seja,o Python alocará memória	suficiente para guardar	todas as informações	da Conta
    dentro da memória do programa.O __new__(), portanto, devolve	uma referência, uma seta que
    aponta	para o objeto em memória	e é guardada na variável conta.

    Tem como objetivo proteger os atributos de manipulações estravagantes, como por exemplo
        Sacar um valor que não esteja disponível na conta;
        Deixa o código mais estruturado e limpo.
        Além de deixar mais claro e flexível na hora de programar. Pois assim como outras linguagens
    Python é uma linguagem que é construído por meio da Orientação a Objeto, identificando classes e métodos
    que podemos utilizar por meio do entendimento da POO.



    Observe que no método __init__() estamos inicializando o valor de limite com 1000,
    ou seja, determinamos um valor base inicial para cada conta (regra de negócio).
    Sendo assim, ao criar uma variável referência do objeto Conta, podemos chamar a classe
    da seguinte forma:

    ` def __init__(self, numero, titular, saldo, limite=1000.00):
            <código omitido>                                      `

    `conta = Conta('1345-9', 'Matheus', 1500)`



    ## Métodos

    São as funcionalidades de uma classe, que são as funções encontradas
    dentro de uma classe.

    Para utilizar o método deposita, utilizamos o '.' por meio do objeto conta
    para chamar o método deposita


    """
    def __init__(self, numero, titular, saldo, limite=1000.00):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        print('Este é o método inicializador')

    """
    
    ## Métodos

    São as funcionalidades de uma classe, que são as funções encontradas
    dentro de uma classe.

    Para utilizar o método deposita, utilizamos o '.' por meio do objeto conta
    para chamar o método deposita

    método depositar: determina o valor a ser depositado na conta. Nesse caso, só temos uma 
    única conta, porem quando temos N contas, podemos criar X instâncias do objeto Conta,
    deixando a programação mais dinâmica.
    
    """

    def deposita(self, valor):
        self.saldo += valor


    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True


    def extrato(self):
        print('Número: {}, \nSaldo: {}'.format(self.numero, self.saldo))


    def transfere_para(self, destino, valor): # conta destino e o valor a ser transferido
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True



"""

A classe cliente será responsável por criar as instâncias de clientes que serão 
vinculados a uma conta.

"""

class Cliente:

    def __init__(self, nome, titular, cpf):
        self.nome = nome
        self.titular = titular
        self.cpf = cpf



class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.now()
        self.transacoes = []

    def imprime(self):
        print('A data da abertura é: {}'.format(self.data_abertura))
        print('Histórico de transações: ')

        for t in self.transacoes:
            print("-", t)



# from conta import Conta

"""
TUDO EM PYTHON É UM OBJETO! sempre que utilizamos uma função em Python ou método que recebe
parâmetros, estamos passando objetos como argumentos.

Portanto podemos entender que um programa orientado a objeto é um grande conjunto de classes
que vai se comunicar delegando responsabilidades para quem for mais apto a realizar determinada tarefa.
A classe Banco delega para a classe Conta que delega para a classe Cliente. Esse sistema, portanto, coabora
trocando mensagens entre si.


class Banco
    class Conta
        class Cliente
            

"""

cliente = Cliente('Matheus', 'Matheus', 123456789)
conta = Conta('123-4', cliente, 1500.00)

print(conta.titular.nome)

print(type(conta.numero)) # <class 'str'>
print(type(conta.saldo)) # <class 'float'>

"""
Quando criamos uma variável para associar ao Objeto Conta, na verdade, essa variável 
não guarda o objeto, e sim uma maneira de acessá-lo, que chamaos de referência (o self)

Portanto, conta e sonho são variáveis referência do Objeto Conta.

"""

" Agor apodemos passar um cliente como parâmetro à criação de uma conta"

cliente = Cliente('Matheus', 'Matheus', 123456789)
conta = Conta('123-4', cliente, 1500)

print(conta.titular.nome)



"""
conta = Conta('1345-9', 'Matheus', 1500)
sonho = Conta('1345-10', 'Matheus', 10000)

print(id(conta)) # 2692262297168
print(id(sonho)) # 2692262297072


conta.transfere_para(sonho, 550.00)

print(sonho.saldo)


print(sonho.limite)

"""

"""

Quando atribuimos conta = sonho,
temos duas instâncias que estão fazendo referência
a um mesmo objeto. Sendo assim os id serão iguais

Obs¹: O operador == compara se as variáveis referências encontram-se no mesmo endereço de memória
e não se eles tem o mesmo valor. 

"""
"""
c1 = Conta('1234-5', 'Matheus', 500.00, 120.00)
c2 = Conta('1234-5', 'Matheus', 500.00, 120.00)
if (c1==c2):
    print('Contas iguais')
else:
    print('Contas em endereços diferentes')

">>> Contas em endereços diferentes"

"""
"""
conta = sonho

print(id(conta)) # 2462778293792
print(id(sonho)) # 2462778293792

"""

