
graph = {
    "livro": {
        "way1": {"obj": "LP", "cost": 3},
        "way2": {"obj": "Poster", "cost": 2},
    },
    "LP": {
        "way1": {"obj": "Bateria", "cost": 10},
        "way2": {"obj": "Baixo", "cost": 2},
    },
    "Poster": {
        "way1": {"obj": "Bateria", "cost": 4},
        "way2": {"obj": "Baixo", "cost": 5},
    },
    "Bateria": {
        "way1": {"obj": "Piano", "cost": 8},
    },
    "Baixo": {
        "way1": {"obj": "Piano", "cost": 8},
    },
}

cost_table = {}

temp_cost_table = {}

graph_iter = iter(graph)

first_key = next(graph_iter)

def new_dict(old_dict: dict):
    new_dict = old_dict.copy()
    del new_dict[first_key]
    return new_dict

for vertice in graph:
    if vertice == first_key:
        cost_table[vertice] = {"father": 0, "cost": 0}
    for way in graph[vertice].values():
        neighbor_1 = way["obj"]
        neighbor_1_cost = way["cost"]
        if vertice == first_key:
            cost_table[neighbor_1] = {"father": vertice, "cost": neighbor_1_cost}

new_graph = new_dict(graph)

for vertice in graph:
    for way in graph[vertice].values():
        neighbor_1 = way["obj"]
        neighbor_1_cost = way["cost"]
        if not neighbor_1 in cost_table:
            cost = neighbor_1_cost + cost_table[vertice]["cost"]
            cost_table[neighbor_1] = {"father": vertice, "cost": cost}
        else:
            cost = neighbor_1_cost + cost_table[vertice]["cost"]
            existed_cost = cost_table[neighbor_1]["cost"]
            existed_father = cost_table[neighbor_1]["father"]
            cost_table[neighbor_1]["cost"] = existed_cost if existed_cost < cost else cost
            cost_table[neighbor_1]["father"] = existed_father if existed_cost < cost else vertice

print(cost_table)
