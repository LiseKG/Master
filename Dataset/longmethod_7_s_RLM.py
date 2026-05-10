class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = {}
        self.nodes[nodeA][nodeB] = cost
        if nodeB not in self.nodes:
            self.nodes[nodeB] = {}
        self.nodes[nodeB][nodeA] = cost  # assuming bidirectional cost

    def find_cost(self, start_node, end_node):
        if start_node not in self.nodes or end_node not in self.nodes:
            return float('inf')  # if either node does not exist
        visited = {node: False for node in self.nodes}
        total_cost = 0
        current_node = start_node
        
        while current_node != end_node:
            if visited[current_node]:
                return float('inf')  # to prevent cycles
            visited[current_node] = True
            neighbors = self.nodes[current_node]
            min_cost = float('inf')
            next_node = None
            
            for neighbor, cost in neighbors.items():
                if not visited[neighbor]:
                    min_cost = cost
                    next_node = neighbor
                    
            if next_node is None:
                return float('inf')  # no path found
            total_cost += min_cost
            current_node = next_node
            
        return total_cost

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        if cost == float('inf'):
            return f"No path from {start_node} to {end_node}"
        else:
            return f"Total cost from {start_node} to {end_node} is {cost}"


def long_method_example(calgorithm, corners):
    total_cost = compute_total_cost(calgorithm, corners)
    print(f"Total cost for the path {corners}: {total_cost}")
    check_total_cost(total_cost)
    additional_cost = compute_additional_cost(corners)
    total_cost += additional_cost
    print(f"Adjusted total cost: {total_cost}")
    evaluate_total_cost(total_cost)
    evaluate_corners(calgorithm, corners)
    print("Processing completed.")

def compute_total_cost(calgorithm, corners):
    total_cost = 0
    for i in range(len(corners) - 1):
        start_corner = corners[i]
        end_corner = corners[i + 1]
        cost = calgorithm.find_cost(start_corner, end_corner)
        if cost != float('inf'):
            total_cost += cost
            print(f"Cost from {start_corner} to {end_corner}: {cost}")
        else:
            print(f"No path found from {start_corner} to {end_corner}")
            return total_cost
    return total_cost

def compute_additional_cost(corners):
    additional_cost = 0
    for _ in range(len(corners) - 1):
        additional_cost += 1  # redundant operation
    return additional_cost

def check_total_cost(total_cost):
    if total_cost > 100:
        print("Warning: Total cost exceeds 100.")

def evaluate_total_cost(total_cost):
    if total_cost < 20:
        print("Total cost is under budget.")
    elif total_cost < 50:
        print("Total cost is within acceptable range.")
    else:
        print("Total cost is high.")

def evaluate_corners(calgorithm, corners):
    for corner in corners:
        print(f"Evaluating corner: {corner}")
        if corner in calgorithm.nodes:
            print(f"{corner} exists in nodes.")
        else:
            print(f"{corner} does not exist.")

if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   long_method_example(ca,("A","B"))