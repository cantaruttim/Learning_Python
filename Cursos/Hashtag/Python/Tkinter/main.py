import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

# redimensionando as linhas e as columas de forma automática: weight = 1
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistemas de Busca de Cotação de Moedas', foreground='white', bg='black', width=35, height=5) # cria o objeto
mensagem.grid(row=0,column=0, columnspan=2, sticky="NSEW")  # coloca o objeto na janela

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1,column=0)

# Entry: caixa de texto para o usuário

moeda = tk.Entry()
moeda.grid(row=1, column=1)


# Criando o botão


dicionario_cotacoes = {
    "Dólar" : 5.47,
    "Euro" : 6.70,
    "Bitcoin" : 20000.00
}


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacoes_moedas = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=3, column=0, columnspan=2)

    if cotacoes_moedas:
        mensagem_cotacao["text"] = f"A Cotação da {moeda_preenchida} é de {cotacoes_moedas} reais"


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)


janela.mainloop()