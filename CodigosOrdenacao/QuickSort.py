from datetime import datetime


class QuickSort:

    def __init__(self):
        self.__trocas = 0
        self.__comparacoes = 0
        self.__tempo_exec = 0

    @property
    def trocas(self):
        return self.__trocas

    @property
    def comparacoes(self):
        return self.__comparacoes

    @property
    def tempo_execucao(self):
        return self.__tempo_exec

    def mediana(self, array, primeiro, segundo, terceiro):
        lista = [float(array[primeiro][2]), float(array[segundo][2]), float(array[terceiro][2])]
        lista.sort()
        if lista[1] == array[primeiro]:
            return primeiro
        elif lista[1] == array[segundo]:
            return segundo
        else:
            return terceiro

    def particao(self, array, esquerda, direita, indice_score):
        # Seleção do pivô. O pivô será o elemento A[esquerda].
        pivo = array[esquerda]
        # Particionamento do arranjo.
        i = esquerda
        j = direita
        while i <= j:
            # Encontra elemento maior que o pivo.
            while array[i][indice_score] <= pivo[indice_score]:
                self.__comparacoes += 1
                i += 1
                if i == direita:
                    break

            # Encontra elemento menor que o pivo.
            while array[j][indice_score] >= pivo[indice_score]:
                self.__comparacoes += 1
                j -= 1
                if j == esquerda:
                    break

            # Ponteiros i e j se cruzaram.
            if i >= j:
                break

            # Troca elementos encontrados acima de lugar.
            array[i], array[j] = array[j], array[i]
            self.__trocas += 1

        # Coloca o pivo no lugar certo.
        aux = array[j]
        array[j] = pivo
        array[esquerda] = aux
        self.__trocas += 1

        # j é o índice em que o pivo agora está.
        return j

    def quicksort(self, array, esquerda, direita, indice_score=2):
        inicio = datetime.now()
        if esquerda >= direita:
            return

        # Calcula a mediana de três elementos.
        m = self.mediana(array, esquerda, (direita - esquerda) // 2, direita)
        # Usa a mediana calculada como pivô.
        array[esquerda], array[m] = array[m], array[esquerda]

        indice_pivo = self.particao(array, esquerda, direita, indice_score)
        self.quicksort(array, esquerda, indice_pivo - 1, indice_score)
        self.quicksort(array, indice_pivo + 1, direita, indice_score)

        fim = datetime.now()
        self.__tempo_exec = fim - inicio


if __name__ == '__main__':
    from Ferramentas.verificaOrdem import verificar
    from Ferramentas.ArquivoToList import organizarEmSublistas
    from os import getcwd, chdir
    
    testequicksort = QuickSort()
    chdir("..")
    lis = organizarEmSublistas(getcwd()+'/data_generation/desordenado/desordenado1.dat')
    testequicksort.quicksort(lis[0], 0, len(lis[0]) - 1, lis[1])

    print("Lista organizada?:", verificar(lis[0], lis[1]))
    print("Trocas:", testequicksort.trocas)
    print("Comparacoes:", testequicksort.comparacoes)
    print(f"Tempo de execução: {testequicksort.tempo_execucao}")
