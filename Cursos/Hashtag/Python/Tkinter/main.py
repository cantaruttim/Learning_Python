import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistemas de Busca de Cotação de Moedas', foreground='white', bg='black', width=35, height=5) # cria o objeto
mensagem.grid(row=0,column=0, columnspan=2, sticky="NSEW")  # coloca o objeto na janela

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1,column=0)

# Entry: caixa de texto para o usuário

moeda = tk.Entry()
moeda.grid(row=1, column=1)



janela.mainloop()