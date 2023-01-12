from Classes import ContaCorrente, CartaoCredito


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







# help(ContaCorrente) podemos dar um help na nossa classe e ele exibe a DocString da classe