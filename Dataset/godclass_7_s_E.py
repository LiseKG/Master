class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        if nodeB not in self.nodes:
            self.nodes[nodeB] = {}
        
        self.nodes[nodeA][nodeB] = cost
        self.nodes[nodeB][nodeA] = cost  # Assuming bidirectional cost

    def find_cost(self, start_node, end_node):
        if start_node in self.nodes and end_node in self.nodes[start_node]:
            return self.nodes[start_node][end_node]
        return -1  # Indicating that a path does not exist

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        return f"Cost from {start_node} to {end_node} is {cost}"

    def add_multiple_nodes(self, connections):
        for a, b, cost in connections:
            self.add_node(a, b, cost)

    def calculate_total_cost(self, corners):
        total_cost = 0
        for i in range(len(corners) - 1):
            cost = self.find_cost(corners[i], corners[i + 1])
            if cost == -1:
                return -1  # Return early if any cost is -1
            total_cost += cost
        return total_cost

    def print_total_cost(self, corners):
        total_cost = self.calculate_total_cost(corners)
        return f"Total cost from {corners} is {total_cost}"

    def get_all_nodes(self):
        return list(self.nodes.keys())

    def is_node_exists(self, node):
        return node in self.nodes

    def clear_nodes(self):
        self.nodes.clear()

    def add_edge_cost(self, nodeA, nodeB, cost):
        self.add_node(nodeA, nodeB, cost)

    def get_neighbors(self, node):
        return list(self.nodes.get(node, {}).keys())

    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
            for n in list(self.nodes.keys()):
                self.nodes[n].pop(node, None)

    def update_cost(self, nodeA, nodeB, new_cost):
        if nodeA in self.nodes and nodeB in self.nodes[nodeA]:
            self.nodes[nodeA][nodeB] = new_cost
            self.nodes[nodeB][nodeA] = new_cost  # Assuming bidirectional

    def get_cost_details(self, nodeA, nodeB):
        cost = self.find_cost(nodeA, nodeB)
        return f"Cost from {nodeA} to {nodeB} is {cost}"

    def total_node_count(self):
        return len(self.nodes)

    def get_all_costs(self):
        costs = {}
        for node, neighbors in self.nodes.items():
            for neighbor, cost in neighbors.items():
                costs[(node, neighbor)] = cost
        return costs

    def average_cost(self):
        total_cost = sum(cost for neighbors in self.nodes.values() for cost in neighbors.values())
        count = sum(len(neighbors) for neighbors in self.nodes.values())
        return total_cost / count if count > 0 else 0

    def check_path_exists(self, start_node, end_node):
        return self.find_cost(start_node, end_node) != -1

    def print_all_nodes(self):
        return f"All nodes: {', '.join(self.get_all_nodes())}"

    def neighbors_count(self, node):
        return len(self.get_neighbors(node))

    def debug_print(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {neighbors}")

    def is_connected(self):
        if not self.nodes:
            return True  # An empty graph is considered connected
        visited = set()
        self._dfs(next(iter(self.nodes)), visited)
        return len(visited) == len(self.nodes)

    def _dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.get_neighbors(node):
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def find_shortest_path(self, start_node, end_node):
        # Placeholder for more complex pathfinding logic
        return f"Shortest path from {start_node} to {end_node} not implemented."

    def total_edges_count(self):
        return sum(len(neighbors) for neighbors in self.nodes.values()) // 2

    def detailed_cost_report(self):
        return "\n".join(f"Edge from {a} to {b}: cost = {cost}" 
                         for (a, b), cost in self.get_all_costs().items())


if __name__ == '__main__':
    algo = CostAlgorithm()

    # add_node
    algo.add_node("A", "B", 5)

    # add_multiple_nodes (also calls add_node internally)
    algo.add_multiple_nodes([
        ("B", "C", 3),
        ("C", "D", 4),
    ])

    # add_edge_cost (calls add_node internally)
    algo.add_edge_cost("D", "E", 2)

    # find_cost
    algo.find_cost("A", "B")

    # print_path_cost (calls find_cost)
    print(algo.print_path_cost("A", "B"))

    # calculate_total_cost (calls find_cost)
    algo.calculate_total_cost(["A", "B", "C"])

    # print_total_cost (calls calculate_total_cost)
    print(algo.print_total_cost(["A", "B", "C"]))

    # get_all_nodes
    algo.get_all_nodes()

    # is_node_exists
    algo.is_node_exists("A")

    # get_neighbors
    algo.get_neighbors("A")

    # neighbors_count (calls get_neighbors)
    algo.neighbors_count("A")

    # update_cost
    algo.update_cost("A", "B", 10)

    # get_cost_details (calls find_cost)
    print(algo.get_cost_details("A", "B"))

    # total_node_count
    algo.total_node_count()

    # get_all_costs
    algo.get_all_costs()

    # average_cost
    algo.average_cost()

    # check_path_exists (calls find_cost)
    algo.check_path_exists("A", "C")

    # print_all_nodes (calls get_all_nodes)
    print(algo.print_all_nodes())

    # debug_print
    algo.debug_print()

    # is_connected (calls _dfs and get_neighbors)
    algo.is_connected()

    # find_shortest_path
    print(algo.find_shortest_path("A", "E"))

    # total_edges_count
    algo.total_edges_count()

    # detailed_cost_report (calls get_all_costs)
    print(algo.detailed_cost_report())

    # remove_node
    algo.remove_node("E")

    # clear_nodes
    algo.clear_nodes()
