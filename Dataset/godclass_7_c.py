# Requirements:
# - Have 8 corners (nodes) with different costs
# - Compute total cost from one point to another
# - The app should take in a list of corners A,B and cost 2. B,C cost 5
# - We should be able to check that the results


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.total_cost = 0


class Edge:
    def __init__(self, node_a, node_b, cost):
        self.node_a = node_a
        self.node_b = node_b
        self.cost = cost


class CostAlgorithm:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.path_log = []
        self.query_history = []

    # Method 1
    def create_node(self, name):
        node = Node(name)
        self.nodes[name] = node
        self.log_event(f"Node '{name}' created.")
        return node

    # Method 2
    def create_edge(self, node_a_name, node_b_name, cost):
        edge = Edge(node_a_name, node_b_name, cost)
        self.edges.append(edge)
        self.log_event(f"Edge {node_a_name}-{node_b_name} with cost {cost} created.")
        return edge

    # Method 3
    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.create_node(nodeA)
        if nodeB not in self.nodes:
            self.create_node(nodeB)
        self.create_edge(nodeA, nodeB, cost)

    # Method 4
    def log_event(self, message):
        self.path_log.append(message)

    # Method 5
    def get_edge_cost(self, node_a_name, node_b_name):
        for edge in self.edges:
            if (edge.node_a == node_a_name and edge.node_b == node_b_name):
                return edge.cost
            if (edge.node_a == node_b_name and edge.node_b == node_a_name):
                return edge.cost
        return None

    # Method 6
    def get_neighbors(self, node_name):
        neighbors = []
        for edge in self.edges:
            if edge.node_a == node_name:
                neighbors.append((edge.node_b, edge.cost))
            elif edge.node_b == node_name:
                neighbors.append((edge.node_a, edge.cost))
        return neighbors

    # Method 7
    def reset_visited(self):
        for node in self.nodes.values():
            node.visited = False
            node.total_cost = 0

    # Method 8
    def find_cost(self, start_node, end_node):
        self.reset_visited()
        if start_node not in self.nodes or end_node not in self.nodes:
            self.log_event(f"Node not found: {start_node} or {end_node}.")
            return -1
        distances = {name: float("inf") for name in self.nodes}
        distances[start_node] = 0
        unvisited = list(self.nodes.keys())
        while unvisited:
            current = min(unvisited, key=lambda n: distances[n])
            if distances[current] == float("inf"):
                break
            if current == end_node:
                break
            for neighbor, cost in self.get_neighbors(current):
                new_cost = distances[current] + cost
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
            unvisited.remove(current)
        result = distances[end_node] if distances[end_node] != float("inf") else -1
        self.record_query(start_node, end_node, result)
        return result

    # Method 9
    def record_query(self, start_node, end_node, result):
        entry = f"{start_node} -> {end_node}: {result}"
        self.query_history.append(entry)
        self.log_event(f"Query recorded: {entry}")

    # Method 10
    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        result = f"Total cost from {start_node} to {end_node}: {cost}"
        print(result)
        return result

    # Method 11
    def show_all_nodes(self):
        names = list(self.nodes.keys())
        print(f"Nodes: {names}")
        return names

    # Method 12
    def show_all_edges(self):
        for edge in self.edges:
            print(f"  {edge.node_a} -- {edge.node_b}: cost {edge.cost}")
        return self.edges

    # Method 13
    def show_graph(self):
        print("Graph overview:")
        self.show_all_nodes()
        self.show_all_edges()

    # Method 14
    def validate_path_exists(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        exists = cost != -1
        status = "reachable" if exists else "unreachable"
        self.log_event(f"{end_node} is {status} from {start_node}.")
        print(f"{end_node} is {status} from {start_node}.")
        return exists

    # Method 15
    def get_cheapest_neighbor(self, node_name):
        neighbors = self.get_neighbors(node_name)
        if not neighbors:
            print(f"{node_name} has no neighbors.")
            return None
        cheapest = min(neighbors, key=lambda x: x[1])
        print(f"Cheapest neighbor of {node_name}: {cheapest[0]} (cost {cheapest[1]})")
        return cheapest

    # Method 16
    def compare_paths(self, start, mid, end):
        direct = self.find_cost(start, end)
        via_mid = self.find_cost(start, mid)
        via_mid2 = self.find_cost(mid, end)
        if via_mid == -1 or via_mid2 == -1:
            via_total = -1
        else:
            via_total = via_mid + via_mid2
        print(f"Direct {start}->{end}: {direct} | Via {mid}: {via_total}")
        self.log_event(f"Compared paths: direct={direct}, via {mid}={via_total}")
        return direct, via_total

    # Method 17
    def show_query_history(self):
        print("Query history:")
        for entry in self.query_history:
            print(f"  {entry}")
        return self.query_history

    # Method 18
    def total_graph_cost(self):
        total = sum(edge.cost for edge in self.edges)
        self.log_event(f"Total graph cost computed: {total}")
        print(f"Total cost of all edges: {total}")
        return total

    # Method 19
    def show_event_log(self):
        print("Event log:")
        for entry in self.path_log:
            print(f"  {entry}")

    # Method 20
    def check_result(self, start_node, end_node, expected_cost):
        actual = self.find_cost(start_node, end_node)
        match = actual == expected_cost
        status = "PASS" if match else f"FAIL (got {actual})"
        self.log_event(f"Check {start_node}->{end_node} expected {expected_cost}: {status}")
        print(f"Check {start_node}->{end_node} expected {expected_cost}: {status}")
        return match

    # Method 21
    def get_node_degree(self, node_name):
        neighbors = self.get_neighbors(node_name)
        degree = len(neighbors)
        print(f"Node '{node_name}' has {degree} connection(s).")
        return degree

    # Method 22
    def summarize(self):
        print(f"Graph has {len(self.nodes)} node(s) and {len(self.edges)} edge(s).")
        self.total_graph_cost()
        self.show_query_history()


if __name__ == "__main__":
    algo = CostAlgorithm()

    # Method 3 - add_node (calls create_node x2, create_edge, log_event)
    # 8 corners: A B C D E F G H
    algo.add_node("A", "B", 2)
    algo.add_node("B", "C", 5)
    algo.add_node("C", "D", 3)
    algo.add_node("D", "E", 4)
    algo.add_node("E", "F", 1)
    algo.add_node("F", "G", 6)
    algo.add_node("G", "H", 2)
    algo.add_node("A", "D", 10)

    # Method 13 - show_graph (calls show_all_nodes, show_all_edges)
    algo.show_graph()

    # Method 10 - print_path_cost (calls find_cost -> reset_visited, get_neighbors, record_query, log_event)
    algo.print_path_cost("A", "C")
    algo.print_path_cost("A", "H")

    # Method 14 - validate_path_exists (calls find_cost, log_event)
    algo.validate_path_exists("A", "H")
    algo.validate_path_exists("B", "G")

    # Method 20 - check_result (calls find_cost, log_event)
    algo.check_result("A", "B", 2)
    algo.check_result("B", "C", 5)
    algo.check_result("A", "C", 7)

    # Method 15 - get_cheapest_neighbor (calls get_neighbors)
    algo.get_cheapest_neighbor("A")
    algo.get_cheapest_neighbor("F")

    # Method 16 - compare_paths (calls find_cost, log_event)
    algo.compare_paths("A", "D", "H")

    # Method 21 - get_node_degree (calls get_neighbors)
    algo.get_node_degree("A")
    algo.get_node_degree("D")

    # Method 22 - summarize (calls total_graph_cost, show_query_history)
    algo.summarize()

    # Method 5 - get_edge_cost (standalone, called directly)
    cost = algo.get_edge_cost("A", "B")
    print(f"Direct edge cost A-B: {cost}")

    # Method 19 - show_event_log (standalone, called directly)
    algo.show_event_log()



