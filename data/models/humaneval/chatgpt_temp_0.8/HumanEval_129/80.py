def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], (i, j), [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        value, (i, j), path = heapq.heappop(heap)
        if len(path) == k:
            return path
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for I, J in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= I < n and 0 <= J < n and (I, J) not in visited:
                heapq.heappush(heap, (grid[I][J], (I, J), path + [grid[I][J]]))
