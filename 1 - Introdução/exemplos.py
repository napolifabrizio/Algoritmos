
### Exemplo de uma pesquisa binária -> 1

## OBS: O algoritmo apenas manipula valores dos index's da lista e confere se o elemento
##      é igual a metade da lista, apenas isso :)

lista_ordenada_1 = [1, 3, 5, 7, 9]

def pesquisa_binaria_1(lista: list, elemento: int):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == elemento:
            return f"Posição: {meio}\nElemento: {lista[meio]}"
        if chute > elemento:
            alto = meio -1
        else:
            baixo = meio + 1
    return None

print(pesquisa_binaria_1(lista_ordenada_1, 3))
