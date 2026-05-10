class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        self.nodes[nodeA][nodeB] = cost

    def find_cost(self, start_node, end_node):
        if start_node in self.nodes and end_node in self.nodes[start_node]:
            return self.nodes[start_node][end_node]
        return float('inf')

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        return str(cost)


def compute_total_cost(cost_algorithm, corners):
    total_cost = 0
    previous_corner = corners[0]
    
    for current_corner in corners[1:]:
        cost = cost_algorithm.find_cost(previous_corner, current_corner)
        total_cost += cost
        
        if current_corner in cost_algorithm.nodes:
            for node in cost_algorithm.nodes[current_corner]:
                # Calculate costs only as necessary
                total_cost += cost_algorithm.find_cost(previous_corner, node)
                total_cost += cost_algorithm.find_cost(current_corner, previous_corner)
                total_cost += cost_algorithm.find_cost(current_corner, current_corner)
                total_cost += cost_algorithm.find_cost(previous_corner, current_corner)

        previous_corner = current_corner

    return total_cost

if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   print(compute_total_cost(ca,("A","B")))