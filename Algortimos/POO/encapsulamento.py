# vamos falar sobre encapsulamento

"""
public, protected, private
"""

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otáveio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rosemary')

print(bd.dados)


