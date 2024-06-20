"""
name: Bryden Mollenauer
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/
https://realpython.com/python-bitwise-operators/
https://www.askpython.com/python/examples/python-bit-manipulation-masking-techniques
https://cs.stackexchange.com/questions/90149/analysis-of-time-complexity-of-travelling-salesman-problem
https://math.libretexts.org/Bookshelves/Applied_Mathematics/Math_in_Society_(Lippman)/06%3A_Graph_Theory/6.06%3A_Hamiltonian_Circuits_and_the_Traveling_Salesman_Problem
https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem.html
https://numpy.org/devdocs/user/absolute_beginners.html
"""
import numpy as np

def parse_tsp_input(input_str):
    """
    Parse the TSP input string into a cost matrix and a mapping of vertices to indices.
    """
    # Split the input string into lines and extract the number of vertices and edges.
    lines = input_str.strip().split("\n")
    num_vertices, num_edges = map(int, lines[0].split())

    # Initialize a mapping from vertex names to indices and a cost matrix.
    vertex_to_index = {}
    vertex_index = 0
    cost_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Parse each edge in the input and populate the cost matrix.
    for line in lines[1:]:
        u, v, cost = line.split()
        if u not in vertex_to_index:
            vertex_to_index[u] = vertex_index
            vertex_index += 1
        if v not in vertex_to_index:
            vertex_to_index[v] = vertex_index
            vertex_index += 1
        i, j = vertex_to_index[u], vertex_to_index[v]
        cost_matrix[i][j] = cost_matrix[j][i] = int(cost)

    # Set the diagonal of the cost matrix to 0 (no cost to stay at the same vertex).
    for i in range(num_vertices):
        cost_matrix[i][i] = 0

    return cost_matrix, vertex_to_index

def held_karp_tsp_with_path_and_reconstruction(cost_matrix):
    n = len(cost_matrix)
    # Initialize dynamic programming and predecessor matrices.
    dp = np.full((1<<n, n), float('inf'))
    dp[1][0] = 0
    predecessor = np.full((1<<n, n), -1)

    # Iterate through subsets of vertices and calculate minimum costs.
    for mask in range(1, 1<<n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) and u != v: #checks if v is in the subset and u and v are not the same
                    if dp[mask][u] > dp[mask ^ (1 << u)][v] + cost_matrix[v][u]: # checks if the current know cost to reach u is more then to reach v + the cost to get to the current place in the graph
                        dp[mask][u] = dp[mask ^ (1 << u)][v] + cost_matrix[v][u]  # updates the mask with the cheapest option
                        predecessor[mask][u] = v
    # Find the minimum cost to complete the tour.
    mask = (1<<n) - 1
    min_cost = float('inf')
    last_vertex = 0
    for i in range(1, n):
        cost = dp[-1][i] + cost_matrix[i][0] #dp[-1][i] is the fastest cost for the cycle
        if cost < min_cost:
            min_cost = cost
            last_vertex = i

    # Reconstruct the path taken for the minimum cost tour.
    path = [0]  # Start from vertex 0
    while mask != 1:
        path.append(last_vertex)
        mask &= ~(1 << last_vertex)
        last_vertex = predecessor[mask | (1 << last_vertex)][last_vertex]
    path.append(0)  # Complete the cycle by returning to vertex 0


    return min_cost, path
def main():
    # Read the number of vertices and edges from standard input.
    num_vertices, num_edges = map(int, input().strip().split())
    tsp_input = f"{num_vertices} {num_edges}\n"
    for _ in range(num_edges):
        tsp_input += input().strip() + "\n"

    # Parse the input, solve the TSP, and reconstruct the path.
    cost_matrix, vertex_to_index = parse_tsp_input(tsp_input)


    min_cost, path_indices = held_karp_tsp_with_path_and_reconstruction(cost_matrix)
    index_to_vertex = {v: k for k, v in vertex_to_index.items()}
    path_names = [index_to_vertex[i] for i in path_indices]

    # Output the minimum cost and the path taken.
    print(int(min_cost))
    print(" ".join(path_names))

if __name__ == '__main__':
    main()
