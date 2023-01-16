# map function
# ela aplica uma função para cada item do seu iterable



def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace('  ', ' ')
    texto = texto.strip()
    return texto



produtos = [' ABCD12 ', 'abcd44', 'abC33  ', '  BeB1514', 'BEEB1244   ']


for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
#print(produtos) # retorna o valor do texto padronizado

# Usando a função map

# cada elemento da minha lista de produtos irá passar pela função padronizar_texto
produtos = list(map(padronizar_texto, produtos))
#print(produtos)


# Lambda Expression
# é uma função anônima, usada quando precisamos retornar apenas um valor

def minha_func(n):
    return n ** 2

print(minha_func(5))


# fazendo por lambda expression

m = lambda n : n ** 2
print(m(5))

