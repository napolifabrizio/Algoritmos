from collections import deque

grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["peggy", "anuj"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

def pesquisa(nome: str, grafo: dict) -> bool:
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if (not pessoa in verificadas) and pessoa_e_vendedor(pessoa):
            print(f"{pessoa} é vendedor de manga!")
            return True
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa)
    return False

# pesquisa("voce", grafo)

grafo_2 = {}

grafo_2["banho"] =["acordar"]
grafo_2["cafe"] = ["escovar"]
grafo_2["escovar"] = ["acordar"]

def ordenar(primeiro: str, grafo: dict) -> list:
    keys = [key for key in grafo.keys()]
    lista_final = [primeiro]
    for valor in grafo.values():
        if valor[0] not in grafo.keys():
            lista_final.append(valor[0])
    while keys:
        key = keys.pop()
        if key in lista_final:
            lista_final.append(grafo[key])
        else:
            keys.append(key)

    return lista_final


ordenar("acordar", grafo_2)