def insertion_sort(lista:list):
    """Retorna a lista organizada, a quantidade de trocas e a quantidade de comparacoes efetuadas. """

    assert len(lista) > 0

    trocas = 0
    comparacoes = 0
    contador = 1
    fim = False
    tamanho_lista = len(lista)

    while not fim:
        fim_da_passada = False
        contador_secundario = contador

        while not fim_da_passada:
            contador_secundario -= 1
            valor_sendo_comparado = float(lista[contador][2])

            # contador secundario anda da direita para a esquerda, comparando os valores anteriores
            comparacoes += 1
            if int(lista[contador_secundario][0]) <= valor_sendo_comparado or contador_secundario < 0:
                # verifica se o numero ja esta na posicao correta a fim de evitar trocas desnecessarias
                if contador_secundario + 1 == contador:
                    fim_da_passada = True

                else:
                    aux = lista[contador]
                    lista.pop(contador)
                    lista = lista[:contador_secundario+1] + [aux] + lista[contador_secundario+1:]

                    trocas += 1
                    fim_da_passada = True

        if contador == tamanho_lista - 1:
            fim = True

        contador += 1

    return lista, trocas, comparacoes


if __name__ == '__main__':
    from Ferramentas.verificaOrdem import verificar
    from Ferramentas.ArquivoToList import organizarEmSublistas

    a_ordenar = [5, 17, 11, 6, 6, 6, 6, 6, 7]

    lista = organizarEmSublistas("/Users/alexecheverria/PycharmProjects/TrabalhoFinalAED/data_generation/"
                                 "desordenado/desordenado1.dat")[1:]
    tupla = insertion_sort(lista)
    print(tupla[0])
    print("Lista esta ordenada?:", verificar(tupla[0]))
    print("Trocas:", tupla[1])
    print("Comparacoes:", tupla[2])
