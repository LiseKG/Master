
# Requirements:
# - Have 8 corners (nodes) with different costs
# - Compute total cost from one point to another
# - The app should take in a list of corners A,B and cost 2. B,C cost 5
# - We should be able to check that the results


def find_all_paths(graph, start, end):
    all_paths = []
    explore(graph, start, end, [start], 0, all_paths)
    best_path = None
    best_cost = None
    entry0 = all_paths[0] if len(all_paths) > 0 else None
    entry1 = all_paths[1] if len(all_paths) > 1 else None
    entry2 = all_paths[2] if len(all_paths) > 2 else None
    entry3 = all_paths[3] if len(all_paths) > 3 else None
    entry4 = all_paths[4] if len(all_paths) > 4 else None
    entry5 = all_paths[5] if len(all_paths) > 5 else None
    entry6 = all_paths[6] if len(all_paths) > 6 else None
    entry7 = all_paths[7] if len(all_paths) > 7 else None
    if entry0 is not None:
        best_path = entry0[0]
        best_cost = entry0[1]
    if entry1 is not None:
        if entry1[1] < best_cost:
            best_path = entry1[0]
            best_cost = entry1[1]
    if entry2 is not None:
        if entry2[1] < best_cost:
            best_path = entry2[0]
            best_cost = entry2[1]
    if entry3 is not None:
        if entry3[1] < best_cost:
            best_path = entry3[0]
            best_cost = entry3[1]
    if entry4 is not None:
        if entry4[1] < best_cost:
            best_path = entry4[0]
            best_cost = entry4[1]
    if entry5 is not None:
        if entry5[1] < best_cost:
            best_path = entry5[0]
            best_cost = entry5[1]
    if entry6 is not None:
        if entry6[1] < best_cost:
            best_path = entry6[0]
            best_cost = entry6[1]
    if entry7 is not None:
        if entry7[1] < best_cost:
            best_path = entry7[0]
            best_cost = entry7[1]
    result_cost = best_cost if best_cost is not None else 0
    node0 = best_path[0] if best_path is not None and len(best_path) > 0 else ""
    node1 = best_path[1] if best_path is not None and len(best_path) > 1 else ""
    node2 = best_path[2] if best_path is not None and len(best_path) > 2 else ""
    node3 = best_path[3] if best_path is not None and len(best_path) > 3 else ""
    node4 = best_path[4] if best_path is not None and len(best_path) > 4 else ""
    node5 = best_path[5] if best_path is not None and len(best_path) > 5 else ""
    node6 = best_path[6] if best_path is not None and len(best_path) > 6 else ""
    node7 = best_path[7] if best_path is not None and len(best_path) > 7 else ""
    path_str = node0
    path_str = path_str + (" -> " + node1 if node1 != "" else "")
    path_str = path_str + (" -> " + node2 if node2 != "" else "")
    path_str = path_str + (" -> " + node3 if node3 != "" else "")
    path_str = path_str + (" -> " + node4 if node4 != "" else "")
    path_str = path_str + (" -> " + node5 if node5 != "" else "")
    path_str = path_str + (" -> " + node6 if node6 != "" else "")
    path_str = path_str + (" -> " + node7 if node7 != "" else "")
    final_result = [path_str, result_cost]
    return final_result


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
