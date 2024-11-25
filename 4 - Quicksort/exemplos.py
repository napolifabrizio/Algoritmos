
nums = [100, 22, 38, 400, 59, 61, 700, 8]

def soma(lista: list) -> int:
    total = 0
    if lista:
        el = lista.pop(len(lista)-1)
        total = el + soma(lista)
    return total

total = soma(nums)
print(total)

nums_2 = [100, 22, 38, 400, 59, 61, 700, 8]

def contar(lista: list) -> int:
    total = 0
    if lista:
        lista.pop(len(lista)-1)
        total = 1 + contar(lista)
    return total

qtde = contar(nums_2)
print(qtde)

nums_3 = [100, 22, 38, 400, 59, 61, 700, 8]

def quicksort(lista: list) -> list:
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = [i for i in lista[1:] if i <= pivo]
    maiores = [i for i in lista[1:] if i > pivo]
    lista_ordenada = quicksort(menores) + [pivo] + quicksort(maiores)
    return lista_ordenada

lista_ordenada = quicksort(nums_3)
print(lista_ordenada)

## Exemplo Quadrado - 145


def highest_square(side_a, side_b):
    if side_a % side_b == 0:
        return side_b
    else:
        side_c = side_a % side_b
        return highest_square(side_b, side_c)


num1 = 1680
num2 = 400

print(highest_square(num1, num2))