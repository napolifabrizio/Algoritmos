
nums = [1, 2, 3, 4, 5, 6]

def soma(lista):
    total = 0
    for el in lista:
        total += el
    return total

total = soma(nums)

def soma_2(lista):
    total = 0
    if lista:
        el = lista.pop(len(lista)-1)
        total = el + soma_2(lista)
    return total

total_2 = soma_2(nums)

print(total)
print(total_2)
