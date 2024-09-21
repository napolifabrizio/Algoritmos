

### Ordenação por seleção

## Buscar o menor item de um array
def buscaMenor(array):
    menor = array[0]
    indice_menor = 0

    for i in range(1, len(array)):
        if menor > array[i]:
            menor = array[i]
            indice_menor = i

    return indice_menor

numeros = [10, 25, 300, 51, 6000, 8, 9, 170]

## Ordena o array
def ordenacaoPorSelecao(array):
    novoArray = []
    for i in range(len(array)):
        menor = buscaMenor(array)
        novoArray.append(array.pop(menor))
    print(novoArray)

print(ordenacaoPorSelecao(numeros))
