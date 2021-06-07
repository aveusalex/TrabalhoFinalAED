import time

trocas = 0
comparacoes = 0
tempo_execucao = 0


def merge_sort(lista, indice_score=2):
    global trocas, comparacoes, tempo_execucao
    # Por causa da recursao, a condicional serve como ponto de parada, ou seja, quando a lista tiver apenas 1 elemento
    # a recursao deve parar.
    if len(lista) > 1:
        # procurar o meio da lista
        meio = len(lista) // 2

        # dividir em duas partes a lista
        parte_esquerda = lista[:meio]
        parte_direita = lista[meio:]

        # recursao para organizar as partes
        merge_sort(parte_esquerda, indice_score)
        merge_sort(parte_direita, indice_score)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(parte_esquerda) and j < len(parte_direita):
            comparacoes += 1
            if float(parte_esquerda[i][indice_score]) < float(parte_direita[j][indice_score]):
                lista[k] = parte_esquerda[i]
                trocas += 1
                i += 1
            else:
                lista[k] = parte_direita[j]
                trocas += 1
                j += 1
            k += 1

        # verificar se algum elemento sobrou em uma lista
        while i < len(parte_esquerda):
            lista[k] = parte_esquerda[i]
            trocas += 1
            i += 1
            k += 1

        while j < len(parte_direita):
            lista[k] = parte_direita[j]
            trocas += 1
            j += 1
            k += 1



# Driver Code
if __name__ == '__main__':
    from Ferramentas.verificaOrdem import verificar
    from Ferramentas.ArquivoToList import organizarEmSublistas

    # Neste caso, o mergesort teve 784,464 trocas e 718,614 comparações.
    # O quicksort teve, no mesmo caso, 148,366 trocas e 1,984,775 comparações->Mais indicado para ordenacao em disco.
    arr = organizarEmSublistas('/Users/heloi/PycharmProjects/pythonProject/TrabalhoFinalAED/data_generation/desordenado/desordenado1.dat')
    inicio = time.time()
    merge_sort(arr[0], arr[1])
    fim = time.time()
    tempo_exec = (fim - inicio)
    print(arr[0])
    print("Lista organizada?:", verificar(arr[0], arr[1]))
    print("Trocas:", trocas)
    print("Comparacoes:", comparacoes)
    if tempo_exec >= 60:
        print(f"Tempo em minutos: {tempo_exec/60:.4f}")
    else:
        print(f"Tempo em segundos: {tempo_exec:.4f}")
