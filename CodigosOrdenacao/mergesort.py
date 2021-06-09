from datetime import datetime


class MergeSort:
    def __init__(self):
        self.__trocas = 0
        self.__comparacoes = 0
        self.__tempo_execucao = 0

    @property
    def trocas(self):
        return self.__trocas

    @property
    def comparacoes(self):
        return self.__comparacoes

    @property
    def tempo_execucao(self):
        return self.__tempo_execucao

    def merge_sort(self, lista, indice_score=2):
        # Por causa da recursao, a condicional serve como ponto de parada, ou seja, quando a lista tiver
        # apenas 1 elemento a recursao deve parar.
        if len(lista) > 1:
            # procurar o meio da lista
            meio = len(lista) // 2

            # dividir em duas partes a lista
            parte_esquerda = lista[:meio]
            parte_direita = lista[meio:]

            # recursao para organizar as partes
            self.merge_sort(parte_esquerda, indice_score)
            self.merge_sort(parte_direita, indice_score)

            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(parte_esquerda) and j < len(parte_direita):
                self.__comparacoes += 1
                if float(parte_esquerda[i][indice_score]) < float(parte_direita[j][indice_score]):
                    lista[k] = parte_esquerda[i]
                    self.__trocas += 1
                    i += 1
                else:
                    lista[k] = parte_direita[j]
                    self.__trocas += 1
                    j += 1
                k += 1

            # verificar se algum elemento sobrou em uma lista
            while i < len(parte_esquerda):
                lista[k] = parte_esquerda[i]
                self.__trocas += 1
                i += 1
                k += 1

            while j < len(parte_direita):
                lista[k] = parte_direita[j]
                self.__trocas += 1
                j += 1
                k += 1


# Driver Code
if __name__ == '__main__':
    from Ferramentas.verificaOrdem import verificar
    from Ferramentas.ArquivoToList import organizarEmSublistas
    from os import getcwd, chdir

    chdir("..")
    arr = organizarEmSublistas(getcwd() + '/data_generation/desordenado/desordenado1.dat')
    metodo_ordenacao = MergeSort()

    # Neste caso, o mergesort teve 784,464 trocas e 718,614 comparações.
    # O quicksort teve, no mesmo caso, 148,366 trocas e 1,984,775 comparações->Mais indicado para ordenacao em disco.
    inicio = datetime.now()
    metodo_ordenacao.merge_sort(arr[0], arr[1])
    fim = datetime.now()
    tempo_exec = fim - inicio

    print("Lista organizada?:", verificar(arr[0], arr[1]))
    print("Trocas:", metodo_ordenacao.trocas)
    print("Comparacoes:", metodo_ordenacao.comparacoes)
    print(f"Tempo de execução: {tempo_exec}")

