# LC é uma forma de percorrer uma lista de valores de uma forma mais direta
# uma única linha de código

"""

preco = [450, 550.25, 156, 3200]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone 3']


impostos = []
for item in preco:
    impostos.append(item * 0.03)
#print(impostos)


impostos_lc = [ preco * 0.3 for preco in preco]
print(impostos_lc)

# podemos utilizar isso com uma função

def imposto(preco, valor_imposto):
    return preco * valor_imposto

imposto_df_LC = [imposto(preco, 0.03) for preco in preco]

#################################################################

preco = [450, 550.25, 156, 3200]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone 3']

lista_aux = list(zip(preco, produtos))

lista_aux.sort(reverse=True)
print(lista_aux)


produtos = [produtos for preco, produtos in lista_aux]
print(produtos)


"""


vendas_produtos = [
                    ('ipod', 55810, 70550), 
                    ('Notebook Asus,GFORCE i7', 110550, 115220), 
                    ('IphoneX', 48655, 38560)

                    ]

listas21 = []
listas22 = []
for produto, vendas21, vendas22 in vendas_produtos:
    listas21.append(vendas21)
    listas22.append(vendas22)

print(listas21, listas22)

# Fazendo com LC
listas21_2 = [vendas21 for produto, vendas21, vendas22 in vendas_produtos]
print(listas21_2)

print(max(listas21_2))
print(min(listas21_2))


# nesse caso, adicionamos o valor do produto assim como o nome do produto.
listas21_2_produtos = [(vendas21,produto) for produto, vendas21, vendas22 in vendas_produtos]
print(listas21_2_produtos)



######## 


# Aplicando condicional no LC


meta = 1000
vendas = [4500, 550.25, 156, 30200]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone 3']


produtos_acima_meta = []
for i, produto in enumerate(produtos):
    if vendas[i] > meta:
        produtos_acima_meta.append(produto)


produtos_acima_meta_lc = [produto for i, produto in enumerate(produtos) if vendas[i] > meta]
#print(produtos_acima_meta_lc)

# Alterando o resultado final 

vendedores = {'Maria':1200, 'Carlos':820, 'Antônia': 1750, 'Matheus':950}
meta = 1000

bonus = []

for item in vendedores:
    if vendedores[item] > meta:
        # encontrando o valor de 10% do valor da venda de cada vendedor
        bonus.append(vendedores[item] * .1)
    else:
        bonus.append(0)

#print(bonus)



bonus_lc = [ vendedores[item] * .1 if vendedores[item] > meta else 0 for item in vendedores ]
print(bonus_lc)


"""
Pontos a se considerar

1. Uso do enumarete em listas

"""