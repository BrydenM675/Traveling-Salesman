import random

class Graph:
    
    # creates a new graph
    def __init__(self):
        self.graph = {}

    # adds edges to graph
    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = {}
        self.graph[start][end] = weight

    # prints graph in the form of 412 input files
    def __str__(self):
        visited = {None}
        print_string = "\n"
        print_string += str(len(self.graph.keys()) * (len(self.graph.keys()) - 1)/2) + "\n"
        for v in self.graph:
            for u in self.graph:
                if u in self.graph[v] and u + v not in visited:
                    visited.add(v + u)
                    print_string += (v + " " + u + " " + str(self.graph[v][u]) + "\n")
        return print_string
    
    # prints graph in the form of an adjacency hash
    def adj_hash(self):
        print_string = "\n"
        for v in self.graph:
            print_string += (v + "  |  ")
            for u in self.graph:
                if u in self.graph[v]:
                    print_string += (u + ": " + str(self.graph[v][u]) + ",  ")
            print_string += "\n"
        return print_string
    
    # produces undirected complete graph with random weights
    # num_nodes maximum number of nodes
    # max_weight maximum weight of edges
    def random(num_nodes, max_weight):
        graph = Graph()
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                weight = random.randint(1, max_weight)
                graph.add_edge(str(i), str(j), weight)
                graph.add_edge(str(j), str(i), weight)
        return graph
    
def main():

    graph = Graph.random(5, 5)
    print(graph.adj_hash())
    print(graph)

if __name__ == "__main__":
    main()