
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


def validate_algorithm(algo,nodes):
    cost_ab = algo.find_cost("A", "B")
    cost_ba = algo.find_cost("B", "A")
    cost_bc = algo.find_cost("B", "C")
    cost_ah = algo.find_cost("A", "H")
    cost_cd = algo.find_cost("C", "D")
    path_ab = f"Cost from A to B: {cost_ab}"

    if nodes is None:
        return False
    if len(nodes) == 0:
        return False
    if cost_ab < 0:
        return False
    if cost_bc < 0:
        return False
    if cost_ab != cost_ba:
        return False
    if nodes.get("A") is None:
        return False
    if nodes.get("B") is None:
        return False
    if cost_ah == 0:
        return False
    if path_ab == "":
        return False
    if nodes.get("C") is None:
        return False
    if cost_cd < 0:
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

    print(validate_algorithm(algo,algo.nodes))


