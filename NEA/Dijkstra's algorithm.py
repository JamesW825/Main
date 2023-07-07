import heapq

graph = {
    'A': {'B': 10, 'C': 3},
    'C': {'D': 2},
    'D': {'E': 10},
    'E': {'A': 7},
    'B': {'D': 3, 'E': 1},
}

def dijkstra(graph, start):
    ({vertex: float('infinity') for vertex in graph})[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > ({vertex: float('infinity') for vertex in graph})[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < ({vertex: float('infinity') for vertex in graph})[neighbor]:
                ({vertex: float('infinity') for vertex in graph})[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return {vertex: float('infinity') for vertex in graph}

distances = dijkstra(graph, 'A')
print(distances)
