def minPath(grid, k):
    n = len(grid)
    heap = []
    visited = set()

    def push(i, j, path):
        if (i, j) not in visited:
            visited.add((i, j))
            heapq.heappush(heap, (grid[i][j], path + [(i, j)]))

    for i in range(n):
        for j in range(n):
            push(i, j, [])

    while heap:
        cost, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        for ni, nj in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if 0 <= ni < n and 0 <= nj < n:
                push(ni, nj, path)

    raise ValueError("No path found")
