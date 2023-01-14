class Meu_Objeto:

    # inicialização da classe
    def __init__(pessoa):
        # criando os atributos do objeto Pessoa
        pessoa.nome = 'Pedro'
        pessoa.idade = 33
        pessoa.peso = 65.8
        pessoa.endereco = 'Rua dos Bananais, 2890'
        print('Chamando o construtor')


    def imprime(pessoa):
        print('Olá meu nome é %s e eu tenho %d' %(pessoa.nome, pessoa.idade))


# Chamando os construtores e atributos

a = Meu_Objeto()

"""

# chamando um método de dentro da minha classe
a.imprime()

# printando algumas atributos da classe
print(a.peso)
print(a.endereco)

# help(Meu_Objeto)


"""