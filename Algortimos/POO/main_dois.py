# Getters and Setters

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * ( percentual/ 100) )



    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter configura o preco
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor



p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

# no caso de deixarmos o preco como string, precisamos filtrar o preco
p2 = Produto('Caneca', 'R$ 35.70')
p2.desconto(10)
print(p2.preco)
