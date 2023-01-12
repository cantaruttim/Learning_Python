from Classes import ContaCorrente, CartaoCredito
from Agencias import Agencia, AgenciaComum, AgenciaPremium, AgenciaVirtual

# PROGRAMA
conta = ContaCorrente('Matheus', '123.456.789 - 11', 1234, 34062)
conta.consultar_saldo() # utilizando o método para consultar saldo

cartao = CartaoCredito('Matheus', conta)

print(cartao.conta_corrente._num_conta)
print(conta._cartoes[0].numero) # o/
print(cartao.validade)
print(cartao.numero)
print(f'O codigo de seguranca é : {cartao.cod_seguranca}')

cartao.senha = '4568'
print(f'A nova senha é : {cartao._senha}')



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







# help(ContaCorrente) podemos dar um help na nossa classe e ele exibe a DocString da classe