import tkinter
from tkinter import ttk


class Janelita:

    def teste(self):
        aux = self.__deseja_salvar.get()
        print(aux)

    def __init__(self):
        janela = tkinter.Tk()
        janela.title("Ordenei! - Métodos de ordenação")

        self.__user = tkinter.StringVar()
        self.__deseja_salvar = tkinter.IntVar()
        self.__dire = tkinter.StringVar()

        self.__quick_sort = tkinter.IntVar()
        self.__merge_sort = tkinter.IntVar()
        self.__insert_sort = tkinter.IntVar()

        ttk.Label(janela, text="Diretório do dataset a ordenar: ").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(janela, text="Diretório da base de salvamento: ").grid(row=2, column=0, padx=10, pady=10)

        ttk.Checkbutton(janela, text="Deseja salvar a ordenação?",
                        variable=self.__deseja_salvar).grid(row=1, column=0, padx=10, pady=10)

        ttk.Entry(janela, textvariable=self.__user).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(janela, textvariable=self.__dire).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(janela, text="").grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(janela, text="\tSelecione quais métodos de ordenação deseja:").grid(row=4, column=0,
                                                                                      padx=10, pady=10)

        ttk.Checkbutton(janela, text="QuickSort    ", variable=self.__quick_sort).grid(row=5, column=0, padx=10, pady=10)
        ttk.Checkbutton(janela, text="MergeSort    ", variable=self.__merge_sort).grid(row=5, column=1, padx=10, pady=10)
        ttk.Checkbutton(janela, text="InsertionSort", variable=self.__insert_sort).grid(row=7, column=0, padx=10, pady=10)

        ttk.Label(janela, text="").grid(row=8, column=0, padx=10, pady=10)

        ttk.Button(janela, text='Ordenar!', command=self.teste).grid(row=9, column=0, padx=10, pady=10)
        ttk.Button(janela, text='Cancelar').grid(row=9, column=1, padx=10, pady=10)

        janela.mainloop()


if __name__ == '__main__':
    Janelita()
