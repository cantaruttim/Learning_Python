import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text='Sistemas de Busca de Cotação de Moedas', foreground='white', bg='black') # cria o objeto
mensagem.pack()  # coloca o objeto na janela

mensagem2 = tk.Label(text='Selecione a moeda desejada', fg='white', bg='black', width=50, height=10)
mensagem2.pack()

janela.mainloop()