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

final_graph = {}

def find_the_lowest_node(costs: dict):
    lowest = ""
    lowest_cost = infinity
    for node in costs:
        if (costs[node] <= lowest_cost) and (node not in processeds):
            lowest = node
            lowest_cost = costs[node]
    return lowest

node = find_the_lowest_node(vertice_costs)

while node is not None:
    if not node:
        break
    for neighboor in graph[node]:
        node_cost = vertice_costs[node]
        neighboor_cost = graph[node][neighboor]
        total_cost = node_cost + neighboor_cost
        if total_cost < vertice_costs[neighboor]:
            vertice_costs[neighboor] = total_cost
            vertice_fathers[neighboor] = node
    processeds.append(node)
    node = find_the_lowest_node(vertice_costs)


print(vertice_fathers)