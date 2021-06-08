import tkinter
from tkinter import ttk


class Janelita:

    def troca(self, info):
        if info == 1:
            self.__erro2.config(text="")
        elif info == 2:
            self.__erro1.config(text="")

    def check(self):
        valida1 = self.__insert_sort.get()
        valida2 = self.__quick_sort.get()
        valida3 = self.__merge_sort.get()
        if not(valida1 or valida2 or valida3):
            self.__erro2.config(text="Selecione ao menos um método de ordenação!")
            self.__janela.after(4000, self.troca, 1)

        else:
            self.ordenar()

    def ordenar(self):
        from Ferramentas.ArquivoToList import organizarEmSublistas
        from datetime import datetime

        # verifica se o diretorio é válido.
        path = self.__diretorio_carregamento.get()
        if path:
            lista = organizarEmSublistas(path)
        else:
            self.__erro1.config(text="Insira um diretório válido!")
            self.__janela.after(4000, self.troca, 2)
            return

        if self.__quick_sort.get():
            from CodigosOrdenacao.QuickSort import quicksort
            self.__begin = datetime.now()
            quicksort(lista[0], 0, len(lista[0])-1, lista[1])
            self.__end = datetime.now()
            self.__tempo_qs = self.__end - self.__begin
            print("quick:", lista[0])
            # Implementar o retorno visual ao cliente
            # limpar a tela do tkinter

        if self.__merge_sort.get():
            from CodigosOrdenacao.mergesort import merge_sort
            # recuperar a lista original
            lista = organizarEmSublistas(path)
            self.__begin = datetime.now()
            merge_sort(lista[0], lista[1])
            self.__end = datetime.now()
            self.__tempo_ms = self.__end - self.__begin
            print("merge:", lista[0])
            # Implementar o retorno visual ao cliente

        if self.__insert_sort.get():
            from CodigosOrdenacao.InsertionSort import insertion_sort
            # recuperar a lista original
            lista = organizarEmSublistas(path)
            self.__begin = datetime.now()
            tupla = insertion_sort(lista[0], lista[1])
            self.__end = datetime.now()
            self.__tempo_is = self.__end - self.__begin
            print("insert:", tupla[0])
            # Implementar o retorno visual ao cliente

    def __init__(self):
        self.__janela = tkinter.Tk()
        self.__janela.title("Ordenei! - Métodos de ordenação")

        self.__diretorio_carregamento = tkinter.StringVar()
        self.__deseja_salvar = tkinter.IntVar()
        self.__diretorio_salvamento = tkinter.StringVar()

        # variaveis booleanas (0 ou 1) para indicar quais algoritmos serão utilizados.
        self.__quick_sort = tkinter.IntVar()
        self.__merge_sort = tkinter.IntVar()
        self.__insert_sort = tkinter.IntVar()

        # tempos de processamento de cada algoritmo
        self.__tempo_qs = 0
        self.__tempo_ms = 0
        self.__tempo_is = 0

        # variaveis auxiliares para marcacao do tempo
        self.__begin = 0
        self.__end = 0

        ttk.Label(self.__janela, text="Diretório do dataset a ordenar: ").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__janela, text="Diretório da base de salvamento: ").grid(row=2, column=0, padx=10, pady=10)
        self.__erro1 = ttk.Label(self.__janela, text="")
        self.__erro1.grid(row=1, column=1, padx=10, pady=10)

        ttk.Checkbutton(self.__janela, text="Deseja salvar a ordenação?",
                        variable=self.__deseja_salvar).grid(row=1, column=0, padx=10, pady=10)

        ttk.Entry(self.__janela, textvariable=self.__diretorio_carregamento).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(self.__janela, textvariable=self.__diretorio_salvamento).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.__janela, text="").grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.__janela, text="\tSelecione quais métodos de ordenação deseja:").grid(row=4, column=0,
                                                                                      padx=10, pady=10)

        ttk.Checkbutton(self.__janela, text="QuickSort    ", variable=self.__quick_sort).grid(row=5, column=0, padx=10, pady=10)
        ttk.Checkbutton(self.__janela, text="MergeSort    ", variable=self.__merge_sort).grid(row=5, column=1, padx=10, pady=10)
        ttk.Checkbutton(self.__janela, text="InsertionSort", variable=self.__insert_sort).grid(row=7, column=0, padx=10, pady=10)

        self.__erro2 = ttk.Label(self.__janela, text="")
        self.__erro2.grid(row=8, column=0, padx=10, pady=10)

        ttk.Button(self.__janela, text='Ordenar!', command=self.check).grid(row=9, column=0, padx=10, pady=10)
        ttk.Button(self.__janela, text='Cancelar').grid(row=9, column=1, padx=10, pady=10)

        self.__janela.mainloop()


if __name__ == '__main__':
    Janelita()
