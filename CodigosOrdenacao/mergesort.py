trocas = 0
comparacoes = 0


def merge_sort(lista):
    global trocas, comparacoes
    # Por causa da recursao, a condicional serve como ponto de parada, ou seja, quando a lista tiver apenas 1 elemento
    # a recursao deve parar.
    if len(lista) > 1:
        # procurar o meio da lista
        meio = len(lista) // 2

        # dividir em duas partes a lista
        parte_esquerda = lista[:meio]
        parte_direita = lista[meio:]

        # recursao para organizar as partes
        merge_sort(parte_esquerda)
        merge_sort(parte_direita)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(parte_esquerda) and j < len(parte_direita):
            comparacoes += 1
            if int(parte_esquerda[i][0]) < int(parte_direita[j][0]):
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
    from verificaOrdem import verificar
    from ArquivoToList import organizarEmSublistas

    arr = organizarEmSublistas("/Users/alexecheverria/Documents/ProgramasPython/AED/data_generation/desordenado/desordenado2.dat")[1:]
    merge_sort(arr)
    print("Lista organizada?:", verificar(arr))
    print("Trocas:", trocas)
    print("Comparacoes:", comparacoes)