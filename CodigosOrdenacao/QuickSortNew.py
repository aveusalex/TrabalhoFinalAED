from datetime import datetime
from Ferramentas.verificaOrdem import verificar
from Ferramentas.ArquivoToList import organizarEmSublistas
from os import getcwd, chdir

comparacoes = 0
trocas = 0

class QuickSort:

    def __init__(self):
        self.trocas = 0
        self.comparacoes = 0
        self.tempo_exec = 0

    def mediana(self,array, primeiro, segundo, terceiro):
        lista = [float(array[primeiro][2]), float(array[segundo][2]), float(array[terceiro][2])]
        lista.sort()
        if lista[1] == array[primeiro]:
            return primeiro
        elif lista[1] == array[segundo]:
            return segundo
        else:
            return terceiro


    def particao(self,Array, esquerda, direita, indice_score):
        # Seleção do pivô. O pivô será o elemento A[esquerda].
        pivo = Array[esquerda]
        # Particionamento do arranjo.
        i = esquerda
        j = direita
        while i <= j:
            # Encontra elemento maior que o pivo.
            while Array[i][indice_score] <= pivo[indice_score]:
                self.comparacoes += 1
                i += 1
                if i == direita:
                    break

            # Encontra elemento menor que o pivo.
            while Array[j][indice_score] >= pivo[indice_score]:
                self.comparacoes += 1
                j -= 1
                if j == esquerda:
                    break

            # Ponteiros i e j se cruzaram.
            if i >= j:
                break

            # Troca elementos encontrados acima de lugar.
            Array[i], Array[j] = Array[j], Array[i]
            self.trocas += 1

        # Coloca o pivo no lugar certo.
        aux = Array[j]
        Array[j] = pivo
        Array[esquerda] = aux
        self.trocas += 1

        # j é o índice em que o pivo agora está.
        return j


    def quicksort(self,Array, esquerda, direita, indice_score=2):
        inicio = datetime.now()
        if esquerda >= direita:
            return

        # Calcula a mediana de três elementos.
        m = self.mediana(Array, esquerda, (direita - esquerda) // 2, direita)
        # Usa a mediana calculada como pivô.
        Array[esquerda], Array[m] = Array[m], Array[esquerda]

        indice_pivo = self.particao(Array, esquerda, direita, indice_score)
        self.quicksort(Array, esquerda, indice_pivo - 1, indice_score)
        self.quicksort(Array, indice_pivo + 1, direita, indice_score)

        fim = datetime.now()
        self.tempo_exec = fim - inicio

if __name__ == '__main__':
    testequicksort = QuickSort()
    chdir("..")
    lista = organizarEmSublistas(getcwd()+'/data_generation/desordenado/desordenado1.dat')
    testequicksort.quicksort(lista[0], 0, len(lista[0])-1, lista[1])


    print("Lista organizada?:", verificar(lista[0], lista[1]))
    print("Trocas:", testequicksort.trocas)
    print("Comparacoes:", testequicksort.comparacoes)
    print(f"Tempo de execução: {testequicksort.tempo_exec}")

