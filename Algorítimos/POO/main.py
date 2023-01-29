from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

# são independentes
p1.falar('POO')
p2.falar('Filmes')

print(p1.ano_atual)
print(p1.get_ano_nascimento())