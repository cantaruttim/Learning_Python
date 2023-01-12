


# criando agencias do banco


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual {}'.format(self.caixa))
        else:
            print('O valor {} do caixa está ok'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa')


    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# Agencia virtual, comum e premium

class AgenciaVirtual(Agencia): # criamos uma subclasse Agencia Virtual
    pass

class AgenciaComum(Agencia):
    pass

class AgenciaPremium(Agencia):
    pass






agencia1 = Agencia(22223333, 123213128367, 5467)
agencia1.caixa = 8777666
print(agencia1.verificar_caixa())


agencia1.emprestar_dinheiro(5000, 12342333, 1.15)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Matheus', 123324312, 600000)
print(agencia1.clientes)


agenciaVirtual = AgenciaVirtual(33342134,1789287328,1)
print(agenciaVirtual)