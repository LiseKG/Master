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
            #self.add_node(start_node,end_node)find_cost
            print("test")
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
                print("node_none")
                return #float('inf')  # no path found
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
    #1
    total_cost = 0
    #2
    for i in range(len(corners) - 1):
        #3
        start_corner = corners[i]
        #4
        end_corner = corners[i + 1]
        #5
        cost = calgorithm.find_cost(start_corner, end_corner)
        #6
        if cost != float('inf'):
            #7
            total_cost += cost
            #8
            print(f"Cost from {start_corner} to {end_corner}: {cost}")
            #9
        else:
            #10
            print(f"No path found from {start_corner} to {end_corner}")
            #11
            return
    #12
    print(f"Total cost for the path {corners}: {total_cost}")
    #13
    if total_cost > 100:
        #14
        print("Warning: Total cost exceeds 100.")
        #15
    additional_cost = 0
    #16
    for i in range(len(corners) - 1):
        #17
        # additional redundancy for demonstration
        additional_cost += 1  # redundant operation
        #18
    #19
    total_cost += additional_cost
    #20
    print(f"Adjusted total cost: {total_cost}")
    #21
    if total_cost < 20:
        #22
        print("Total cost is under budget.")
        #23
    elif total_cost < 50:
        #24
        print("Total cost is within acceptable range.")
        #25
    else:
        #26
        print("Total cost is high.")
        #27
    #28
    for corner in corners:
        #29
        print(f"Evaluating corner: {corner}")
        #30
        # adding more redundant checks
        if corner in calgorithm.nodes:
            #31
            print(f"{corner} exists in nodes.")
            #32
        else:
            #33
            print(f"{corner} does not exist.")
            #34
    #35
    print("Processing completed.")


if __name__ == '__main__':
   ca = CostAlgorithm()
   ca.add_node("A","B",5)
   print(ca.find_cost("A","B"))
   print(ca.print_path_cost("A","B"))
   long_method_example(ca,("A","B"))