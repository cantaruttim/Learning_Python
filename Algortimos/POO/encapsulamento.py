# vamos falar sobre encapsulamento

"""
public, protected, private

convensões:
1. _
2. __
"""

class BaseDeDados:
    def __init__(self):
        self.dados = {} #atributo public

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rosemary')
bd.inserir_cliente(4, 'Fernando')

# bd.dados = 'Uma outra coisa ... ' quebra a classe inteira
bd.lista_clientes()

print(bd.dados)

"""
quando temos um underline na frente da instância, 
recomenda-se não acessar esse atributo ex: _dados (_protected_)

"""


