def floyd_warshall(graph):
    V = len(graph)  # Find the number of vertices
    dist = [[float('inf')] * V for _ in range(V)]  # Initialize distance matrix
    
    # Initialize the distance matrix with the graph values
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # Floyd-Warshall Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def main():
    V = int(input("Enter the number of offices: "))
    vertices = []
    graph = []
    
    # Input office names
    print("Enter the names of the offices:")
    for _ in range(V):
        vertices.append(input())
    
    # Input the cost matrix
    print("Enter the cost matrix (use 'inf' for no connection):")
    for i in range(V):
        row = []
        for j in range(V):
            if i == j:
                row.append(0)  # The cost to reach itself is 0
            else:
                print(f"Cost from {vertices[i]} to {vertices[j]}: ", end="")
                cost = input()
                # Assign 'inf' if no connection, otherwise parse the cost as an integer
                row.append(float('inf') if cost == 'inf' else int(cost))
        graph.append(row)

    # Get the shortest path matrix using Floyd-Warshall
    shortest_paths = floyd_warshall(graph)
    
    # Output the shortest path cost matrix
    print("The shortest path cost matrix is:")
    for i in range(V):
        print(f"From {vertices[i]}: ", end="")
        print(" ".join(str(shortest_paths[i][j]) for j in range(V)))

# Main entry point of the script
if __name__ == "__main__":
    main()

