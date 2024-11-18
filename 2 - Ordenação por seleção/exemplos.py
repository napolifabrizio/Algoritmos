import time
from decimal import Decimal
import array as arr

### Ordenação por seleção

## Buscar o menor item de uma lista
def buscaMenor(array):
    menor = array[0]
    indice_menor = 0

    for i in range(1, len(array)):
        if menor > array[i]:
            menor = array[i]
            indice_menor = i

    return indice_menor

numeros = [10, 25, 300, 51, 6000, 8, 9, 170]

## Ordena a lista
def ordenacaoPorSelecao(lista):
    nova_lista = []
    for i in range(len(lista)):
        menor = buscaMenor(lista)
        nova_lista.append(lista.pop(menor))
    print(nova_lista)

# print(ordenacaoPorSelecao(numeros))

### Comparações Array x Lista

def append_item_list():
    data_list = []
    t0 = time.time()
    for x in range(1, 1000000):
        data_list.append(x)
    # print(data_list)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

def append_item_array():
    data_array = arr.array("i", [])
    t0 = time.time()
    for x in range(1, 1000000):
        data_array.append(x)
    # print(data_array)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

def search_item_list():
    data_list = [x for x in range(1, 100000000)]
    t0 = time.time()
    item = data_list[len(data_list) - 1]
    print(item)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

def search_item_array():
    data = [x for x in range(1, 100000000)]
    data_array = arr.array("i", data)
    t0 = time.time()
    item = data_array[len(data_array) - 1]
    print(item)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

def delete_item_array():
    data = [x for x in range(1, 10000000)]
    data_array = arr.array("i", data)
    t0 = time.time()
    data_array.pop(700000)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

def delete_item_list():
    data_list = [x for x in range(1, 10000000)]
    t0 = time.time()
    data_list.pop(700000)
    t1 = time.time()
    res = Decimal(t1 - t0)
    return res

# Comparações

def compare_append():
    time_array = append_item_array()
    time_list = append_item_list()

    winner = "Array" if time_array < time_list else "List"
    print(winner)

def compare_search(): # sendo analisado ainda
    time_array = search_item_array()
    time_list = search_item_list()

    winner = "Array" if time_array < time_list else "List"
    print(winner)

def compare_delete():
    time_array = delete_item_array()
    time_list = delete_item_list()

    winner = "Array" if time_array < time_list else "List"
    print(winner)

compare_search()

