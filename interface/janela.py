import tkinter
from tkinter import ttk


janela = tkinter.Tk()
janela.title("Ordenei! - Métodos de ordenation")

user = tkinter.StringVar()
senha = tkinter.StringVar()
dire = tkinter.StringVar()
link = tkinter.StringVar()
qtd_pessoas = tkinter.StringVar()
qtd_comment = tkinter.StringVar()
frase_antes = tkinter.StringVar()
nome_strvar = tkinter.StringVar()

ttk.Label(janela, text="Usuário: ").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(janela, text="Senha: ").grid(row=1, column=0, padx=10, pady=10)
ttk.Label(janela, text="Diretório da base: ").grid(row=2, column=0, padx=10, pady=10)
ttk.Label(janela, text="Link sorteio: ").grid(row=3, column=0, padx=10, pady=10)
ttk.Label(janela, text="Qtd pessoas por comentário: ").grid(row=4, column=0, padx=10, pady=10)
ttk.Label(janela, text="Qtd de comentários: ").grid(row=5, column=0, padx=10, pady=10)
ttk.Label(janela, text="Frase antes: ").grid(row=6, column=0, padx=10, pady=10)
ttk.Label(janela, text="Nome de salvamento: ").grid(row=7, column=0, padx=10, pady=10)
ttk.Entry(janela, textvariable=user).grid(row=0, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=senha).grid(row=1, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=dire).grid(row=2, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=link).grid(row=3, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=qtd_pessoas).grid(row=4, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=qtd_comment).grid(row=5, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=frase_antes).grid(row=6, column=1, padx=10, pady=10)
ttk.Entry(janela, textvariable=nome_strvar).grid(row=7, column=1, padx=10, pady=10)
ttk.Button(janela, text='Iniciar').grid(row=8, column=1, padx=10, pady=10)
ttk.Button(janela, text='Cancelar').grid(row=8, column=0, padx=10, pady=10)
ttk.Button(janela, text='Salvar').grid(row=8, column=2, padx=10, pady=10)
ttk.Button(janela, text='Carregar').grid(row=8, column=3, padx=10, pady=10)

janela.mainloop()