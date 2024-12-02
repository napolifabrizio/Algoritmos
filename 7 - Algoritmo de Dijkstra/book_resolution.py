graph = {
    "inicio": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fim": 1,
        "c": 3,
    },
    "b": {
        "a": 3,
        "fim": 5,
        "d": 2
    },
    "c": {
        "fim": 4
    },
    "d": {
        "fim": 3
    },
    "fim": {}
}

infinity = float("inf")

vertice_costs = {
    "a": 6,
    "b": 2,
    "c": infinity,
    "d": infinity,
    "fim": infinity,
}

vertice_fathers = {
    "a": "inicio",
    "b": "inicio",
    "c": "",
    "d": "",
    "fim": "",
}

processeds = []

def find_lowest_cost(costs: dict):
    lowest_cost = infinity
    lowest_nodo_cost = None
    for nodo in costs:
        cost = costs[nodo]
        if cost <= lowest_cost and nodo not in processeds:
            lowest_cost = cost
            lowest_nodo_cost = nodo
    return lowest_nodo_cost

nodo = find_lowest_cost(vertice_costs)

while nodo is not None:
    cost = vertice_costs[nodo]
    neighbors = graph[nodo]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if vertice_costs[n] > new_cost:
            vertice_costs[n] = new_cost
            vertice_fathers[n] = nodo
    processeds.append(nodo)
    nodo = find_lowest_cost(vertice_costs)

# print(vertice_costs)
print(vertice_fathers)