# LC é uma forma de percorrer uma lista de valores de uma forma mais direta
# uma única linha de código



preco = [450, 550.25, 156, 325]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone 3']


impostos = []
for item in preco:
    impostos.append(item * 0.03)
print(impostos)


impostos_lc = [ preco * 0.3 for preco in preco]
print(impostos_lc)