# Possible solution using Dijkstra's algorithm

import heapq

def minPath(grid, k):
    # Define the graph
    n = len(grid)
    graph = {(i, j): [] for i in range(n) for j in range(n)}
    for i in range(n):
        for j in range(n):
            if i > 0:
                graph[(i, j)].append(((i - 1, j), grid[i - 1][j]))
            if i < n - 1:
                graph[(i, j)].append(((i + 1, j), grid[i + 1][j]))
            if j > 0:
                graph[(i, j)].append(((i, j - 1), grid[i][j - 1]))
            if j < n - 1:
                graph[(i, j)].append(((i, j + 1), grid[i][j + 1]))
                
    # Find the minimum path using Dijkstra's algorithm
    start = (0, 0)
    heap = [(0, start, [grid[0][0]])]
    visited = set()
    while heap:
        (cost, curr, path) = heapq.heappop(heap)
        if len(path) == k:
            return path
        if curr in visited:
            continue
        visited.add(curr)
        for (next, value) in graph[curr]:
            heapq.heappush(heap, (cost + value, next, path + [value]))
