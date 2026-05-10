# File energy refactored version: godclass_7_s_RGC_E.py

class NodeManager:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        # Using setdefault to reduce duplication of conditional checks
        self.nodes.setdefault(nodeA, {})[nodeB] = cost
        self.nodes.setdefault(nodeB, {})[nodeA] = cost  # Assuming bidirectional cost

    def find_cost(self, start_node, end_node):
        # Simplified cost retrieval with early return
        return self.nodes.get(start_node, {}).get(end_node, -1)

    def is_node_exists(self, node):
        # Directly return existence check
        return node in self.nodes

    def clear_nodes(self):
        self.nodes.clear()

    def get_neighbors(self, node):
        # Return neighbors directly or empty list
        return list(self.nodes.get(node, {}).keys())

    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
            # Using a set to reduce lookup time
            for n in list(self.nodes.keys()):
                self.nodes[n].pop(node, None)  # Remove the reference to the deleted node

    def update_cost(self, nodeA, nodeB, new_cost):
        if nodeA in self.nodes and nodeB in self.nodes[nodeA]:
            self.nodes[nodeA][nodeB] = self.nodes[nodeB][nodeA] = new_cost  # Bi-directional update

    def total_node_count(self):
        return len(self.nodes)

    def get_cost_details(self, nodeA, nodeB):
        return f"Cost from {nodeA} to {nodeB} is {self.find_cost(nodeA, nodeB)}"

    def average_cost(self):
        # Using a generator to avoid creating large intermediate lists
        costs = [cost for neighbors in self.nodes.values() for cost in neighbors.values()]
        return sum(costs) / len(costs) if costs else 0

    def neighbors_count(self, node):
        # Directly return length of neighbors
        return len(self.get_neighbors(node))

    def total_edges_count(self):
        # Using sum and dictionary view to avoid double counting
        return sum(len(neighbors) for neighbors in self.nodes.values()) // 2

    def debug_print(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {neighbors}")

    def is_connected(self):
        visited = set()
        # Handle empty node set
        if not self.nodes:
            return True

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
        # Use zip for reducing the traversal of the list
        return sum(self.node_manager.find_cost(a, b) for a, b in zip(corners, corners[1:]))

    def print_total_cost(self, corners):
        total_cost = self.calculate_total_cost(corners)
        return f"Total cost from {corners} is {total_cost}"

    def print_path_cost(self, start_node, end_node):
        cost = self.node_manager.find_cost(start_node, end_node)
        return f"Cost from {start_node} to {end_node} is {cost}"

    def check_path_exists(self, start_node, end_node):
        # Simplified existence check
        return self.node_manager.find_cost(start_node, end_node) != -1

    def detailed_cost_report(self):
        # Efficient dictionary compilation
        costs = self.get_all_costs()
        return "\n".join(f"Edge from {a} to {b}: cost = {cost}" for (a, b), cost in costs.items())

    def get_all_costs(self):
        # Avoid double counting edges
        costs = {}
        for node, neighbors in self.node_manager.nodes.items():
            for neighbor, cost in neighbors.items():
                if (neighbor, node) not in costs:  # Avoid reverse duplicates
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
    node_manager.nodes.keys()

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
    print("All nodes: ", ", ".join(node_manager.nodes.keys()))

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
