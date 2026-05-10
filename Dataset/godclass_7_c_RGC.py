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


class GraphBuilder:
    def __init__(self, path_log):
        self.nodes = {}
        self.edges = []
        self.path_log = path_log

    def create_node(self, name):
        node = Node(name)
        self.nodes[name] = node
        self.path_log.append(f"Node '{name}' created.")
        return node

    def create_edge(self, node_a_name, node_b_name, cost):
        edge = Edge(node_a_name, node_b_name, cost)
        self.edges.append(edge)
        self.path_log.append(f"Edge {node_a_name}-{node_b_name} with cost {cost} created.")
        return edge

    def add_node(self, nodeA, nodeB, cost):
        if nodeA not in self.nodes:
            self.create_node(nodeA)
        if nodeB not in self.nodes:
            self.create_node(nodeB)
        self.create_edge(nodeA, nodeB, cost)

    def get_edge_cost(self, node_a_name, node_b_name):
        for edge in self.edges:
            if (edge.node_a == node_a_name and edge.node_b == node_b_name):
                return edge.cost
            if (edge.node_a == node_b_name and edge.node_b == node_a_name):
                return edge.cost
        return None

    def get_neighbors(self, node_name):
        neighbors = []
        for edge in self.edges:
            if edge.node_a == node_name:
                neighbors.append((edge.node_b, edge.cost))
            elif edge.node_b == node_name:
                neighbors.append((edge.node_a, edge.cost))
        return neighbors

    def reset_visited(self):
        for node in self.nodes.values():
            node.visited = False
            node.total_cost = 0


class PathFinder:
    def __init__(self, graph: GraphBuilder, path_log, query_history):
        self.graph = graph
        self.path_log = path_log
        self.query_history = query_history

    def record_query(self, start_node, end_node, result):
        entry = f"{start_node} -> {end_node}: {result}"
        self.query_history.append(entry)
        self.path_log.append(f"Query recorded: {entry}")

    def find_cost(self, start_node, end_node):
        self.graph.reset_visited()
        if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
            self.path_log.append(f"Node not found: {start_node} or {end_node}.")
            return -1
        distances = {name: float("inf") for name in self.graph.nodes}
        distances[start_node] = 0
        unvisited = list(self.graph.nodes.keys())
        while unvisited:
            current = min(unvisited, key=lambda n: distances[n])
            if distances[current] == float("inf"):
                break
            if current == end_node:
                break
            for neighbor, cost in self.graph.get_neighbors(current):
                new_cost = distances[current] + cost
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
            unvisited.remove(current)
        result = distances[end_node] if distances[end_node] != float("inf") else -1
        self.record_query(start_node, end_node, result)
        return result

    def print_path_cost(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        result = f"Total cost from {start_node} to {end_node}: {cost}"
        print(result)
        return result

    def validate_path_exists(self, start_node, end_node):
        cost = self.find_cost(start_node, end_node)
        exists = cost != -1
        status = "reachable" if exists else "unreachable"
        self.path_log.append(f"{end_node} is {status} from {start_node}.")
        print(f"{end_node} is {status} from {start_node}.")
        return exists

    def get_cheapest_neighbor(self, node_name):
        neighbors = self.graph.get_neighbors(node_name)
        if not neighbors:
            print(f"{node_name} has no neighbors.")
            return None
        cheapest = min(neighbors, key=lambda x: x[1])
        print(f"Cheapest neighbor of {node_name}: {cheapest[0]} (cost {cheapest[1]})")
        return cheapest

    def compare_paths(self, start, mid, end):
        direct = self.find_cost(start, end)
        via_mid = self.find_cost(start, mid)
        via_mid2 = self.find_cost(mid, end)
        if via_mid == -1 or via_mid2 == -1:
            via_total = -1
        else:
            via_total = via_mid + via_mid2
        print(f"Direct {start}->{end}: {direct} | Via {mid}: {via_total}")
        self.path_log.append(f"Compared paths: direct={direct}, via {mid}={via_total}")
        return direct, via_total

    def check_result(self, start_node, end_node, expected_cost):
        actual = self.find_cost(start_node, end_node)
        match = actual == expected_cost
        status = "PASS" if match else f"FAIL (got {actual})"
        self.path_log.append(f"Check {start_node}->{end_node} expected {expected_cost}: {status}")
        print(f"Check {start_node}->{end_node} expected {expected_cost}: {status}")
        return match

    def get_node_degree(self, node_name):
        neighbors = self.graph.get_neighbors(node_name)
        degree = len(neighbors)
        print(f"Node '{node_name}' has {degree} connection(s).")
        return degree


class GraphReporter:
    def __init__(self, graph: GraphBuilder, path_log, query_history):
        self.graph = graph
        self.path_log = path_log
        self.query_history = query_history

    def show_all_nodes(self):
        names = list(self.graph.nodes.keys())
        print(f"Nodes: {names}")
        return names

    def show_all_edges(self):
        for edge in self.graph.edges:
            print(f"  {edge.node_a} -- {edge.node_b}: cost {edge.cost}")
        return self.graph.edges

    def show_graph(self):
        print("Graph overview:")
        self.show_all_nodes()
        self.show_all_edges()

    def show_query_history(self):
        print("Query history:")
        for entry in self.query_history:
            print(f"  {entry}")
        return self.query_history

    def total_graph_cost(self):
        total = sum(edge.cost for edge in self.graph.edges)
        self.path_log.append(f"Total graph cost computed: {total}")
        print(f"Total cost of all edges: {total}")
        return total

    def show_event_log(self):
        print("Event log:")
        for entry in self.path_log:
            print(f"  {entry}")

    def summarize(self):
        print(f"Graph has {len(self.graph.nodes)} node(s) and {len(self.graph.edges)} edge(s).")
        self.total_graph_cost()
        self.show_query_history()


class CostAlgorithm:
    def __init__(self):
        self.path_log = []
        self.query_history = []
        self.graph = GraphBuilder(self.path_log)
        self.finder = PathFinder(self.graph, self.path_log, self.query_history)
        self.reporter = GraphReporter(self.graph, self.path_log, self.query_history)


if __name__ == "__main__":
    algo = CostAlgorithm()

    # Method 3 - add_node (calls create_node x2, create_edge, log_event)
    # 8 corners: A B C D E F G H
    algo.graph.add_node("A", "B", 2)
    algo.graph.add_node("B", "C", 5)
    algo.graph.add_node("C", "D", 3)
    algo.graph.add_node("D", "E", 4)
    algo.graph.add_node("E", "F", 1)
    algo.graph.add_node("F", "G", 6)
    algo.graph.add_node("G", "H", 2)
    algo.graph.add_node("A", "D", 10)

    # Method 13 - show_graph (calls show_all_nodes, show_all_edges)
    algo.reporter.show_graph()

    # Method 10 - print_path_cost (calls find_cost -> reset_visited, get_neighbors, record_query, log_event)
    algo.finder.print_path_cost("A", "C")
    algo.finder.print_path_cost("A", "H")

    # Method 14 - validate_path_exists (calls find_cost, log_event)
    algo.finder.validate_path_exists("A", "H")
    algo.finder.validate_path_exists("B", "G")

    # Method 20 - check_result (calls find_cost, log_event)
    algo.finder.check_result("A", "B", 2)
    algo.finder.check_result("B", "C", 5)
    algo.finder.check_result("A", "C", 7)

    # Method 15 - get_cheapest_neighbor (calls get_neighbors)
    algo.finder.get_cheapest_neighbor("A")
    algo.finder.get_cheapest_neighbor("F")

    # Method 16 - compare_paths (calls find_cost, log_event)
    algo.finder.compare_paths("A", "D", "H")

    # Method 21 - get_node_degree (calls get_neighbors)
    algo.finder.get_node_degree("A")
    algo.finder.get_node_degree("D")

    # Method 22 - summarize (calls total_graph_cost, show_query_history)
    algo.reporter.summarize()

    # Method 5 - get_edge_cost (standalone, called directly)
    cost = algo.graph.get_edge_cost("A", "B")
    print(f"Direct edge cost A-B: {cost}")

    # Method 19 - show_event_log (standalone, called directly)
    algo.reporter.show_event_log()



