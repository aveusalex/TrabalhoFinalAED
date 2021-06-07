from datetime import datetime

comparacoes = 0
trocas = 0

def mediana(array, primeiro, segundo, terceiro):
    lista = [float(array[primeiro][2]), float(array[segundo][2]), float(array[terceiro][2])]
    lista.sort()
    if lista[1] == array[primeiro]:
        return primeiro
    elif lista[1] == array[segundo]:
        return segundo
    else:
        return terceiro


def particao(Array, esquerda, direita, indice_score):
    global comparacoes, trocas
    # Seleção do pivô. O pivô será o elemento A[esquerda].
    pivo = Array[esquerda]
    # Particionamento do arranjo.
    i = esquerda
    j = direita
    while i <= j:
        # Encontra elemento maior que o pivo.
        while Array[i][indice_score] <= pivo[indice_score]:
            comparacoes += 1
            i += 1
            if i == direita:
                break

        # Encontra elemento menor que o pivo.
        while Array[j][indice_score] >= pivo[indice_score]:
            comparacoes += 1
            j -= 1
            if j == esquerda:
                break

        # Ponteiros i e j se cruzaram.
        if i >= j:
            break

        # Troca elementos encontrados acima de lugar.
        Array[i], Array[j] = Array[j], Array[i]
        trocas += 1

    # Coloca o pivo no lugar certo.
    aux = Array[j]
    Array[j] = pivo
    Array[esquerda] = aux
    trocas += 1

    # j é o índice em que o pivo agora está.
    return j


def quicksort(Array, esquerda, direita, indice_score=2):
    if esquerda >= direita:
        return

    # Calcula a mediana de três elementos.
    m = mediana(Array, esquerda, (direita - esquerda) // 2, direita)
    # Usa a mediana calculada como pivô.
    Array[esquerda], Array[m] = Array[m], Array[esquerda]

    indice_pivo = particao(Array, esquerda, direita, indice_score)
    quicksort(Array, esquerda, indice_pivo - 1, indice_score)
    quicksort(Array, indice_pivo + 1, direita, indice_score)


if __name__ == '__main__':
    from Ferramentas.verificaOrdem import verificar
    from Ferramentas.ArquivoToList import organizarEmSublistas
    from os import getcwd, chdir

    chdir("..")
    lista = organizarEmSublistas(getcwd()+'/data_generation/desordenado/desordenado1.dat')
    inicio = datetime.now()
    quicksort(lista[0], 0, len(lista[0])-1, lista[1])
    fim = datetime.now()
    tempo_exec = fim - inicio
    print(lista[0])

    print("Lista organizada?:", verificar(lista[0], lista[1]))
    print("Trocas:", trocas)
    print("Comparacoes:", comparacoes)
    print(f"Tempo de execução: {tempo_exec}")

