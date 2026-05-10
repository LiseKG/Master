class NodeManager:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        self.nodes[nodeA][nodeB] = cost
        
        if nodeB not in self.nodes:
            self.nodes[nodeB] = {}
        self.nodes[nodeB][nodeA] = cost  # Assuming bidirectional cost

    def find_cost(self, start_node, end_node):
        if start_node not in self.nodes or end_node not in self.nodes:
            return -1
        return self.nodes[start_node].get(end_node, -1)

    def get_all_nodes(self):
        return list(self.nodes.keys())

    def is_node_exists(self, node):
        return node in self.nodes

    def clear_nodes(self):
        self.nodes.clear()

    def get_neighbors(self, node):
        return list(self.nodes.get(node, {}).keys())

    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
            for n in self.nodes:
                if node in self.nodes[n]:
                    del self.nodes[n][node]

    def update_cost(self, nodeA, nodeB, new_cost):
        if nodeA in self.nodes and nodeB in self.nodes[nodeA]:
            self.nodes[nodeA][nodeB] = new_cost
            self.nodes[nodeB][nodeA] = new_cost  # Assuming bidirectional

    def total_node_count(self):
        return len(self.nodes)

    def get_cost_details(self, nodeA, nodeB):
        return f"Cost from {nodeA} to {nodeB} is {self.find_cost(nodeA, nodeB)}"

    def average_cost(self):
        total_cost = sum(cost for neighbor in self.nodes.values() for cost in neighbor.values())
        count = sum(len(neighbor) for neighbor in self.nodes.values())
        return total_cost / count if count > 0 else 0

    def neighbors_count(self, node):
        return len(self.get_neighbors(node))

    def total_edges_count(self):
        return sum(len(neighbors) for neighbors in self.nodes.values()) // 2

    def debug_print(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {neighbors}")

    def is_connected(self):
        visited = set()
        self.dfs(next(iter(self.nodes)), visited)
        return len(visited) == len(self.nodes)

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.get_neighbors(node):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


class CostAlgorithm:
    def __init__(self):
        self.node_manager = NodeManager()

    def get_node_manager(self):
        return self.node_manager

    def calculate_total_cost(self, corners):
        total_cost = 0
        for i in range(len(corners) - 1):
            total_cost += self.node_manager.find_cost(corners[i], corners[i + 1])
        return total_cost

    def print_total_cost(self, corners):
        total_cost = self.calculate_total_cost(corners)
        return f"Total cost from {corners} is {total_cost}"

    def print_path_cost(self, start_node, end_node):
        cost = self.node_manager.find_cost(start_node, end_node)
        return f"Cost from {start_node} to {end_node} is {cost}"

    def check_path_exists(self, start_node, end_node):
        return self.node_manager.find_cost(start_node, end_node) != -1

    def detailed_cost_report(self):
        report = []
        for (a, b), cost in self.get_all_costs().items():
            report.append(f"Edge from {a} to {b}: cost = {cost}")
        return "\n".join(report)

    def get_all_costs(self):
        costs = {}
        for node, neighbors in self.node_manager.nodes.items():
            for neighbor, cost in neighbors.items():
                costs[(node, neighbor)] = cost
        return costs


if __name__ == '__main__':
    algo = CostAlgorithm()
    node_manager = algo.get_node_manager()

    # add_node
    node_manager.add_node("A", "B", 5)

    # add_multiple_nodes (also calls add_node internally)
    node_manager.add_node("B", "C", 3)
    node_manager.add_node("C", "D", 4)

    # add_edge_cost (calls add_node internally)
    node_manager.add_node("D", "E", 2)

    # find_cost
    node_manager.find_cost("A", "B")

    # print_path_cost (calls find_cost)
    print(algo.print_path_cost("A", "B"))

    # calculate_total_cost (calls find_cost)
    algo.calculate_total_cost(["A", "B", "C"])

    # print_total_cost (calls calculate_total_cost)
    print(algo.print_total_cost(["A", "B", "C"]))

    # get_all_nodes
    node_manager.get_all_nodes()

    # is_node_exists
    node_manager.is_node_exists("A")

    # get_neighbors
    node_manager.get_neighbors("A")

    # neighbors_count (calls get_neighbors)
    algo.node_manager.neighbors_count("A")

    # update_cost
    node_manager.update_cost("A", "B", 10)

    # get_cost_details (calls find_cost)
    print(algo.print_path_cost("A", "B"))

    # total_node_count
    node_manager.total_node_count()

    # get_all_costs
    algo.get_all_costs()

    # average_cost
    algo.node_manager.average_cost()

    # check_path_exists (calls find_cost)
    algo.check_path_exists("A", "C")

    # print_all_nodes (calls get_all_nodes)
    print("All nodes: ", ", ".join(node_manager.get_all_nodes()))

    # debug_print
    node_manager.debug_print()

    # is_connected (calls _dfs and get_neighbors)
    print("Is connected:", node_manager.is_connected())

    # find_shortest_path
    print(algo.check_path_exists("A", "E"))

    # total_edges_count
    print("Total edges count:", node_manager.total_edges_count())

    # detailed_cost_report (calls get_all_costs)
    print(algo.detailed_cost_report())

    # remove_node
    node_manager.remove_node("E")

    # clear_nodes
    node_manager.clear_nodes()
