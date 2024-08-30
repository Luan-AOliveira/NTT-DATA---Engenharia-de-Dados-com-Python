def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def test(a, b):
    return a*2 + b*3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 18, somar) # O resultado da operação 10 + 18 = 28
exibir_resultado(10, 18, subtrair) # O resultado da operação 10 - 18 = -8
exibir_resultado(10, 18, test) # O resultado da operação (10x2) + (18x3) = 74



op = somar
print(op(1, 23))
