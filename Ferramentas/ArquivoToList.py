def arquivoToList(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()

    return linhas


def organizarEmSublistas(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()

    aux = 0
    for elemento in linhas:
        novo_elemento = elemento.split()
        linhas[aux] = novo_elemento
        aux += 1

    cabecalho = linhas[0]
    indice_score = 0
    for elemento in cabecalho:
        if elemento == "SCORE":
            break
        elif indice_score == len(cabecalho) - 1:
            indice_score = 2
            break
        indice_score += 1

    linhas.pop(0)

    return linhas, indice_score


if __name__ == '__main__':
    lista = organizarEmSublistas("/Users/alexecheverria/Documents/ProgramasPython/AED/"
                                 "data_generation/desordenado/desordenado2.dat")
    print(lista[1:3])
