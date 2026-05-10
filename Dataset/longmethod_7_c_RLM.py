
# Requirements:
# - Have 8 corners (nodes) with different costs
# - Compute total cost from one point to another
# - The app should take in a list of corners A,B and cost 2. B,C cost 5
# - We should be able to check that the results


def find_all_paths(graph, start, end):
    all_paths = []
    explore(graph, start, end, [start], 0, all_paths)
    best_path, best_cost = None, None
    for path, cost in all_paths:
        if best_cost is None or cost < best_cost:
            best_path, best_cost = path, cost
    result_cost = best_cost if best_cost is not None else 0
    path_str = " -> ".join(best_path) if best_path else ""
    return [path_str, result_cost]


def explore(graph, current, end, path, cost, all_paths):
    if current == end:
        all_paths.append((path, cost))
    neighbors = graph.get(current, {})
    for neighbor in neighbors:
        if neighbor not in path:
            edge_cost = neighbors[neighbor]
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            explore(graph, neighbor, end, new_path, new_cost, all_paths)


class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        if nodeB not in self.nodes:
            self.nodes[nodeB] = {}
        self.nodes[nodeA][nodeB] = cost
        self.nodes[nodeB][nodeA] = cost

    def find_cost(self, start_node, end_node):
        result = find_all_paths(self.nodes, start_node, end_node)
        return result[1]

    def print_path_cost(self, start_node, end_node):
        result = find_all_paths(self.nodes, start_node, end_node)
        return str(result[1])


if __name__ == "__main__":
    algo = CostAlgorithm()
    algo.add_node("A", "B", 2)
    algo.add_node("B", "C", 5)
    algo.add_node("C", "D", 3)
    algo.add_node("D", "E", 4)
    algo.add_node("E", "F", 1)
    algo.add_node("F", "G", 6)
    algo.add_node("G", "H", 2)
    algo.add_node("A", "C", 10)

    print(algo.find_cost("A", "C"))
    print(algo.print_path_cost("A", "H"))

