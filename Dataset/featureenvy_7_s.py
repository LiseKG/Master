class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        self.nodes[nodeA][nodeB] = cost

    def find_cost(self, start_node, end_node):
        # Simple example logic to find the cost (not complete)
        if start_node in self.nodes and end_node in self.nodes[start_node]:
            return self.nodes[start_node][end_node]
        return float('inf')  # If there's no direct cost, return infinity

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        return str(cost)

def compute_total_cost(cost_algorithm, corners):
    total_cost = 0
    previous_corner = corners[0]
    
    for current_corner in corners[1:]:
        cost = cost_algorithm.find_cost(previous_corner, current_corner)
        total_cost += cost
        # Excessive usage of the CostAlgorithm attributes/methods
        if current_corner in cost_algorithm.nodes:
            for node in cost_algorithm.nodes[current_corner]:
                total_cost += cost_algorithm.nodes[current_corner][node]  # Line 1
                if previous_corner in cost_algorithm.nodes and node in cost_algorithm.nodes[previous_corner]:
                    total_cost += cost_algorithm.nodes[previous_corner][node]  # Line 2
                # Additional lines that contribute to feature envy
                total_cost += cost_algorithm.find_cost(previous_corner, node)  # Line 3
                total_cost += cost_algorithm.print_path_cost(previous_corner, node)  # Line 4
                total_cost += cost_algorithm.nodes[current_corner][node]  # Line 5
                total_cost += cost_algorithm.find_cost(current_corner, previous_corner)  # Line 6
                total_cost += cost_algorithm.print_path_cost(current_corner, previous_corner)  # Line 7
                total_cost += cost_algorithm.nodes[previous_corner][current_corner]  # Line 8
                total_cost += cost_algorithm.nodes[current_corner][previous_corner]  # Line 9
                total_cost += cost_algorithm.find_cost(current_corner, current_corner)  # Line 10
                total_cost += cost_algorithm.print_path_cost(current_corner, current_corner)  # Line 11
                
        previous_corner = current_corner

    return total_cost

if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   print(compute_total_cost(ca,("A","B")))