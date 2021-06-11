import platform
import tkinter
from tkinter import ttk
from sys import setrecursionlimit

aux_n_clientes = 0

setrecursionlimit(10**9)


class Janelita:

    def nome_arq(self):
        nome = self.__diretorio_carregamento.get()
        sistema = platform.system()
        if sistema == "Windows":
            return nome.split("\\")[-1]
        else:
            return nome.split("/")[-1]

    def janela_de_informacoes(self, info: dict):
        janela2 = tkinter.Tk()

        janela2.title("Informações")
        ttk.Separator(janela2, orient='vertical')

        # titulos do merge, quick e insertion
        if self.__quick_sort.get():
            ttk.Label(janela2, text="QuickSort:").grid(row=0, column=0, padx=100, pady=20)
            ttk.Label(janela2, text=f'Arquivo: {self.nome_arq()}').grid(row=1, column=0)
            ttk.Label(janela2, text=f'Tamanho do arquivo: {self.__tamanho_arquivo}').grid(row=2, column=0)
            ttk.Label(janela2, text=f"Trocas: {info['quick'][0]}").grid(row=3, column=0)
            ttk.Label(janela2, text=f"Comparações: {info['quick'][1]}").grid(row=4, column=0)
            ttk.Label(janela2, text=f"Tempo corrido: {self.__tempo_qs}").grid(row=5, column=0)
            ttk.Separator(janela2, orient='vertical').grid(sticky='ns', row=0, rowspan=10, column=1)

        if self.__merge_sort.get():
            ttk.Label(janela2, text="MergeSort:").grid(row=0, column=2, padx=100, pady=20)
            ttk.Label(janela2, text=f'Arquivo: {self.nome_arq()}').grid(row=1, column=2)
            ttk.Label(janela2, text=f'Tamanho do arquivo: {self.__tamanho_arquivo}').grid(row=2, column=2)
            ttk.Label(janela2, text=f"Trocas: {info['merge'][0]}").grid(row=3, column=2)
            ttk.Label(janela2, text=f"Comparações: {info['merge'][1]}").grid(row=4, column=2)
            ttk.Label(janela2, text=f"Tempo corrido: {self.__tempo_ms}").grid(row=5, column=2)
            ttk.Separator(janela2, orient='vertical').grid(sticky='ns', row=0, rowspan=10, column=3)

        if self.__insert_sort.get():
            ttk.Label(janela2, text="InsertionSort:").grid(row=0, column=4, padx=100, pady=20)
            ttk.Label(janela2, text=f'Arquivo: {self.nome_arq()}').grid(row=1, column=4)
            ttk.Label(janela2, text=f'Tamanho do arquivo: {self.__tamanho_arquivo}').grid(row=2, column=4)
            ttk.Label(janela2, text=f"Trocas: {info['insertion'][0]}").grid(row=3, column=4)
            ttk.Label(janela2, text=f"Comparações: {info['insertion'][1]}").grid(row=4, column=4)
            ttk.Label(janela2, text=f"Tempo corrido: {self.__tempo_is}").grid(row=5, column=4)


    def salvar(self, lista):
        self.__ja_salvou = True
        lista_aux = lista[::-1]
        with open(self.__diretorio_salvamento.get(), "w") as file:
            for elemento in lista_aux[:aux_n_clientes]:
                aux = 0
                for unidade in elemento:
                    if not(aux == len(elemento)-1):
                        elemento[aux] = unidade + " "
                    else:
                        elemento[aux] = unidade + "\n"
                    aux += 1

    def troca(self, info):
        if info == 1:
            self.__erro2.config(text="")
        elif info == 2:
            self.__erro1.config(text="")

    def check(self):
        valida1 = self.__insert_sort.get()
        valida2 = self.__quick_sort.get()
        valida3 = self.__merge_sort.get()
        valida4 = self.__deseja_salvar.get()

        if not(valida1 or valida2 or valida3):
            self.__erro2.config(text="Selecione ao menos um método de ordenação!")
            self.__janela.after(4000, self.troca, 1)

        elif valida4 and not self.__diretorio_salvamento.get():
            self.__erro1.config(text="Insira um diretório de salvamento válido!")
            self.__janela.after(4000, self.troca, 2)

        else:
            self.ordenar()

    def ordenar(self):
        from Ferramentas.ArquivoToList import organizarEmSublistas
        from datetime import datetime
        trocas_comparacoes = {"quick": [int, int], "merge": [int, int], "insertion": [int, int]}

        # verifica se o diretorio é válido.
        path = self.__diretorio_carregamento.get()
        if path:
            lista = organizarEmSublistas(path)
            self.__tamanho_arquivo = len(lista[0])
        else:
            self.__erro1.config(text="Insira um diretório válido!")
            self.__janela.after(4000, self.troca, 2)
            return

        # verifica se o número de clientes a serem visualizados é válido
        '''if aux_n_clientes is int:
            pass
        else:
            self.__erro3.config(text="Insira um número inteiro!")
            self.__janela.after(4000,self.troca,2)
            return'''

        if self.__quick_sort.get():
            from CodigosOrdenacao.QuickSort import QuickSort
            # quick sort usa a variavel lista que acabou de ser montada
            quick = QuickSort()
            self.__begin = datetime.now()
            quick.quicksort(lista[0], 0, len(lista[0])-1, lista[1])
            self.__end = datetime.now()
            self.__tempo_qs = self.__end - self.__begin
            # salvar o numero de trocas e comparacoes no dicionario
            trocas_comparacoes["quick"] = [quick.trocas, quick.comparacoes]

            # salvar em um arquivo:
            if self.__deseja_salvar.get() and not self.__ja_salvou:
                self.salvar(lista[0])

        if self.__merge_sort.get():
            from CodigosOrdenacao.mergesort import MergeSort
            # recuperar a lista original
            lista = organizarEmSublistas(path)
            merge = MergeSort()
            self.__begin = datetime.now()
            merge.merge_sort(lista[0], lista[1])
            self.__end = datetime.now()
            self.__tempo_ms = self.__end - self.__begin
            # salvar o numero de trocas e comparacoes no dicionario
            trocas_comparacoes["merge"] = [merge.trocas, merge.comparacoes]

            # salvar em um arquivo:
            if self.__deseja_salvar.get() and not self.__ja_salvou:
                self.salvar(lista[0])


        if self.__insert_sort.get():
            from CodigosOrdenacao.InsertionSort import insertion_sort
            # recuperar a lista original
            lista = organizarEmSublistas(path)
            self.__begin = datetime.now()
            tupla = insertion_sort(lista[0], lista[1])
            self.__end = datetime.now()
            self.__tempo_is = self.__end - self.__begin
            # salvar o numero de trocas e comparacoes no dicionario
            trocas_comparacoes["insertion"] = [tupla[1], tupla[2]]

            # salvar em um arquivo:
            if self.__deseja_salvar.get() and not self.__ja_salvou:
                self.salvar(tupla[0])


        self.janela_de_informacoes(trocas_comparacoes)
        self.__ja_salvou = False


    def __init__(self):
        self.__janela = tkinter.Tk()
        self.__janela.title("Ordenei! - Métodos de ordenação")

        self.__diretorio_carregamento = tkinter.StringVar()
        self.__deseja_salvar = tkinter.IntVar()
        self.__diretorio_salvamento = tkinter.StringVar()
        self.__n_clientes = tkinter.IntVar()
        # controle de salvamento para evitar salvar varias vezes:
        self.__ja_salvou = False

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

        ttk.Checkbutton(self.__janela, text="QuickSort    ", variable=self.__quick_sort).grid(row=5, column=0,
                                                                                              padx=10, pady=10)
        ttk.Checkbutton(self.__janela, text="MergeSort    ", variable=self.__merge_sort).grid(row=5, column=1,
                                                                                              padx=10, pady=10)
        ttk.Checkbutton(self.__janela, text="InsertionSort", variable=self.__insert_sort).grid(row=7, column=0,
                                                                                               padx=10, pady=10)

        ttk.Label(self.__janela, text="Digite o número de clientes com o melhor SCORE que deseja visualizar: ").grid(row=8, column=0, padx=10, pady=10)
        ttk.Entry(self.__janela, textvariable=self.__n_clientes).grid(row=8, column=1, padx=10, pady=10)
        self.__erro3 = ttk.Label(self.__janela, text="")
        self.__erro3.grid(row=7, column=1, padx=10, pady=10)
        aux_n_clientes = self.__n_clientes.get()
        print(aux_n_clientes)

        self.__erro2 = ttk.Label(self.__janela, text="")
        self.__erro2.grid(row=9, column=0, padx=10, pady=10)

        ttk.Button(self.__janela, text='Ordenar!', command=self.check).grid(row=9, column=0, padx=10, pady=10)
        ttk.Button(self.__janela, text='Cancelar', command=self.__janela.quit).grid(row=9, column=1, padx=10, pady=10)

        self.__janela.mainloop()


if __name__ == '__main__':
    Janelita()
