def verificar(lista):
    for i in range(len(lista)):
        if i+1 == len(lista):
            return True

        if int(lista[i+1][0]) - int(lista[i][0]) < 0:
            return False


if __name__ == '__main__':
    teste = [0, 1, 2, 3, 4]
    teste2 = [-1, -2, 4, 5, 7]
    teste3 = [-10, -9, -1, 0]
    teste4 = [-2, -3]
    teste5 = [-9, -7, 0, 10]

    print(verificar(teste))
    print(verificar(teste2))
    print(verificar(teste3))
    print(verificar(teste4))
    print(verificar(teste5))
