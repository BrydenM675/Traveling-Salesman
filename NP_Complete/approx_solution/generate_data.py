import sys
import random
import time
import matplotlib.pyplot as plt 

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

    # Code to create the line plot
    x = [0]
    y = [0]
    a = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    b = [0.00603, 0.00652, 0.00671, 0.00868, 0.01419, 0.02545,
            0.05117, 0.10998, 0.23751, 0.51356, 1.51025, 4.7451,
            9.2581, 19.1334]
    for i in range(1, 12):
        graph = Graph.random(2**i, 50)
        start_time = time.time()
        graph.nearest_neighbor()
        end_time = time.time()
        total_time = end_time - start_time
        x.append(2**i)
        y.append(total_time)

        print(i, total_time)

    plt.plot(x, y) 
    
    plt.xlabel('Input Size (n)') 
    plt.ylabel('Time (seconds)') 
    plt.title('Approximate Complexity') 
    
    plt.show()

    plt.plot(a, b) 
    plt.xlabel('Input Size (n)') 
    plt.ylabel('Time (seconds)') 
    plt.title('Exact Complexity') 
    
    plt.show()

    a = [0, 5, 10, 15, 20]
    b = [0, 15, 274, 303, 371]
    c = [0, 15, 202, 189, 255]

    plt.plot(a, b, label="Approximate") 
    plt.plot(a, c, label="Exact")
    plt.legend()
    plt.xlabel('Input Size (n)') 
    plt.ylabel('Shortest Path') 
    plt.title('Result Comparison') 
    
    plt.show()


if __name__ == "__main__":
    main()