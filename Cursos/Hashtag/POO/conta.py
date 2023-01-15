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



    ## Métodos

    São as funcionalidades de uma classe, que são as funções encontradas
    dentro de uma classe.

    Para utilizar o método deposita, utilizamos o '.' por meio do objeto conta
    para chamar o método deposita


    """
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
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



# from conta import Conta

"""
Quando criamos uma variável para associar ao Objeto Conta, na verdade, essa variável 
não guarda o objeto, e sim uma maneira de acessá-lo, que chamaos de referência (o self)

Portanto, conta e sonho são variáveis referência do Objeto Conta.

"""

conta = Conta('1345-9', 'Matheus', 1500, 3500)
sonho = Conta('1345-10', 'Matheus', 10000, 4000)

print(id(conta)) # 2692262297168
print(id(sonho)) # 2692262297072

"""

Quando atribuimos conta = sonho,
temos duas instâncias que estão fazendo referência
a um mesmo objeto. Sendo assim os id serão iguais

"""

conta = sonho

print(id(conta)) # 2462778293792
print(id(sonho)) # 2462778293792