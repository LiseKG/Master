
# Requirements:
# - Have 8 corners (nodes) with different costs
# - Compute total cost from one point to another
# - The app should take in a list of corners A,B and cost 2. B,C cost 5
# - We should be able to check that the results


class CostAlgorithm:
    def __init__(self):
        self.nodes = {}

    def add_node(self, nodeA,nodeB,cost):
        pass

    def find_cost(self, start_node, end_node):
        pass
        #should return an int

    def print_path_cost(self, start_node, end_node):
        pass
        #should return an string containing an int. 
