import sys

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = {}
        self.graph[start][end] = weight

    def __str__(self):
        visited = {None}
        n = len(self.graph.keys())
        print_string = ""
        print_string += str(n) + " " + str(int((n * (n - 1)) / 2)) + "\n"
        for v in self.graph:
            for u in self.graph:
                if u in self.graph[v] and u + v not in visited:
                    visited.add(v + u)
                    print_string += (v + " " + u + " " + str(self.graph[v][u]) + "\n")
        return print_string
    
    def adj_hash(self):
        print_string = "\n"
        for v in self.graph:
            print_string += (v + "  |  ")
            for u in self.graph:
                if u in self.graph[v]:
                    print_string += (u + ": " + str(self.graph[v][u]) + ",  ")
            print_string += "\n"
        return print_string
    
    def random(num_nodes, max_weight):
        graph = Graph()
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                weight = random.randint(1, max_weight)
                graph.add_edge("index_" + str(i), "index_" + str(j), weight)
                graph.add_edge("index_" + str(j), "index_" + str(i), weight)
        return graph
            

    def nearest_neighbor(self):
        start_node = list(self.graph.keys())[0]

        num_nodes = len(self.graph.keys())
        curr_node = start_node
        visited = {curr_node}
        path = [curr_node]
        total_cost = 0

        for _ in range(num_nodes):
            min_cost = float('inf')
            min_node = None

            for u in self.graph[curr_node]:
                if (u not in visited) and (self.graph[curr_node][u] < min_cost):
                    min_cost = self.graph[curr_node][u]
                    min_node = u
            
            if min_node is not None:
                visited.add(min_node)
                path.append(min_node)
                total_cost += min_cost
                curr_node = min_node
        
        path.append(start_node)
        total_cost += self.graph[curr_node][start_node]

        return path, total_cost
        

def main():

    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        input = file.readline().strip().split()
        m = int(input[1])
        graph = Graph()
        for _ in range(m):
            u, v, w = file.readline().strip().split()
            graph.add_edge(u, v, float(w))
            graph.add_edge(v, u, float(w))
    
    path, price = graph.nearest_neighbor()
    print("{:.4f}".format(price))
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()