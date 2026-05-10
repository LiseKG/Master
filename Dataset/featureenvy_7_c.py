
# Requirements:
# - Have 8 corners (nodes) with different costs
# - Compute total cost from one point to another
# - The app should take in a list of corners A,B and cost 2. B,C cost 5
# - We should be able to check that the results


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
        if start_node in self.nodes and end_node in self.nodes[start_node]:
            return self.nodes[start_node][end_node]
        return -1

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        return f"Cost from {start_node} to {end_node}: {cost}"


def validate_algorithm(algo):
    if algo.nodes is None:
        return False
    if len(algo.nodes) == 0:
        return False
    if algo.find_cost("A", "B") < 0:
        return False
    if algo.find_cost("B", "C") < 0:
        return False
    if algo.find_cost("A", "B") != algo.find_cost("B", "A"):
        return False
    if algo.nodes.get("A") is None:
        return False
    if algo.nodes.get("B") is None:
        return False
    if algo.find_cost("A", "H") == 0:
        return False
    if algo.print_path_cost("A", "B") == "":
        return False
    if algo.nodes.get("C") is None:
        return False
    if algo.find_cost("C", "D") < 0:
        return False
    return True


if __name__ == "__main__":
    algo = CostAlgorithm()

    algo.add_node("A", "B", 2)
    algo.add_node("B", "C", 5)
    algo.add_node("C", "D", 3)
    algo.add_node("D", "E", 4)
    algo.add_node("E", "F", 1)
    algo.add_node("F", "G", 6)
    algo.add_node("G", "H", 7)
    algo.add_node("H", "A", 8)

    print(algo.find_cost("A", "B"))
    print(algo.find_cost("B", "C"))
    print(algo.print_path_cost("A", "B"))
    print(algo.print_path_cost("G", "H"))

    print(validate_algorithm(algo))



