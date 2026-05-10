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
    
    for i in range(len(corners) - 1):
        previous_corner = corners[i]
        current_corner = corners[i + 1]
        cost = cost_algorithm.find_cost(previous_corner, current_corner)
        total_cost += cost
        
        # The excessive nested loops and function calls were removed. 
        # The function now only computes the total cost based on direct paths without redundancy.
    
    return total_cost


if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   print(compute_total_cost(ca,("A","B")))