


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

from random import randint

# Agencia virtual, comum e premium
# Conceeito de Herança

class AgenciaVirtual(Agencia): # criamos uma subclasse Agencia Virtual
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000) # precisamos fazer isso para mantermos o valor dos atributos da super classe
        self.caixa = 1000000
        self.caixa_paypal = 0

    # Métodos que só existem dentro do escopo da Agência Virtual

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem patrimônio mínimo necessário para entrar na Agência Premium')






agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 976886655, 17890000177)
print(agencia_virtual.site)
print(agencia_virtual.caixa)

agencia_comum = AgenciaComum(45678877, 278098887746)
agencia_comum.verificar_caixa()

agencia_premium = AgenciaPremium(76896655, 18934549897)
agencia_premium.verificar_caixa()


agencia1 = Agencia(22223333, 123213128367, 5467)
agencia1.caixa = 8777666
print(agencia1.verificar_caixa())


agencia1.emprestar_dinheiro(5000, 12342333, 1.15)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Matheus', 123324312, 600000)
print(agencia1.clientes)


agenciaVirtual = AgenciaVirtual(33342134,1789287328,1)
print(agenciaVirtual)