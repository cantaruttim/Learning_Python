# LC é uma forma de percorrer uma lista de valores de uma forma mais direta
# uma única linha de código



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