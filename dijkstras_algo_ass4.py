import heapq

def network_delay_time(times, N, K):
    # Create a graph as an adjacency list
    graph = {i: [] for i in range(1, N + 1)}
    
    # Populate the graph with the times data
    for u, v, w in times:
        graph[u].append((v, w))

    # Min-heap to store the (time, node) pairs
    min_heap = [(0, K)]  # (time, node)
    
    # Initialize distances with infinity
    distances = {i: float('inf') for i in range(1, N + 1)}
    distances[K] = 0

    # Dijkstra's algorithm using a priority queue (min-heap)
    while min_heap:
        current_time, current_node = heapq.heappop(min_heap)

        if current_time > distances[current_node]:
            continue

        for neighbor, travel_time in graph[current_node]:
            time = current_time + travel_time

            if time < distances[neighbor]:
                distances[neighbor] = time
                heapq.heappush(min_heap, (time, neighbor))

    # Find the maximum time from all distances
    max_time = max(distances.values())

    # Return the result
    return max_time if max_time != float('inf') else -1

if __name__ == "__main__":
    N = int(input("Enter the number of nodes: "))
    M = int(input("Enter the number of edges: "))
    
    times = []
    print("Enter the edges (u, v, w) one per line:")
    for _ in range(M):
        u, v, w = map(int, input().split())
        times.append((u, v, w))

    K = int(input("Enter the starting node K: "))
    
    result = network_delay_time(times, N, K)
    print("The time it takes for all nodes to receive the signal:", result)

