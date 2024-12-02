
infinity = float("inf")

test = {
    "c": infinity,
    "d": infinity,
    "fim": infinity,
}

processeds = []

def find_the_lowest_node(costs: dict):
    lowest = ""
    lowest_cost = infinity
    for node in costs:
        if (costs[node] <= lowest_cost) and (node not in processeds):
            lowest = node
            lowest_cost = costs[node]
    return lowest

print(find_the_lowest_node(test))