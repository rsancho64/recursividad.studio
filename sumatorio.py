from esListaEnterosValida import esListaEnterosValida


def sumatorio(lista):
    if not esListaEnterosValida(lista):
        raise ValueError("lista chunga")
    total = 0
    for item in lista:
        total += item
    return total


def sumatorioREC(lista):

    if not esListaEnterosValida(lista):
        raise ValueError("lista chunga")

    if not lista:
        return 0  # trivial 0
    if 1 == len(lista):
        return lista[0]  # trivial 1
    return lista[0] + sumatorioREC(lista[1:])


if __name__ == "__main__":

    lista = [11, 22, 33, 44, 55]     # 0.. 11..  33..  66.. 110.. 165 (total)
    lista = [11, 22, "cucu", 44, 55]
    lista = [11]
    lista = []

    # print(sumatorio(lista))  ## 165
    print(sumatorioREC(lista))  # 165
