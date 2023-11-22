

def factorialIterativo(n):
    retorno = 1
    factor = 2
    while factor <= n:
        retorno = retorno * factor
        factor += 1
    return retorno


def factorialRecursivo(n):
    if n == 0:
        return 1  # trivial
    return n * factorialRecursivo(n-1)


if __name__ == "__main__":

    # print(factorialIterativo(4))  # 24
    # print(factorialIterativo(3))  # 6
    # print(factorialIterativo(2))  # 2
    # print(factorialIterativo(1))  # 1
    # print(factorialIterativo(0))  # 1

    print(factorialRecursivo(4))  # 24
    # print(factorialRecursivo(3))  # 6
    # print(factorialRecursivo(2))  # 2
    # print(factorialRecursivo(1))  # 1
    # print(factorialRecursivo(0))  # 1
