class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        self.nodes[nodeA][nodeB] = cost

    def find_cost(self, start_node, end_node):
        # Return the cost if available, otherwise infinity
        return self.nodes.get(start_node, {}).get(end_node, float('inf'))

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        return str(cost)


def compute_total_cost(cost_algorithm, corners):
    total_cost = 0
    previous_corner = corners[0]
    
    # Calculate costs for each segment
    for current_corner in corners[1:]:
        cost = cost_algorithm.find_cost(previous_corner, current_corner)
        if cost != float('inf'):
            total_cost += cost
        
        # Calculate adjacent costs only when necessary
        if current_corner in cost_algorithm.nodes:
            for node in cost_algorithm.nodes[current_corner]:
                # We only add necessary costs without redundancy
                total_cost += cost_algorithm.find_cost(previous_corner, node)
        
        previous_corner = current_corner

    return total_cost

if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   print(compute_total_cost(ca,("A","B")))