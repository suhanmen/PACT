def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], [(i, j)]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        _, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < n and 0 <= nj < n:
                heapq.heappush(heap, (grid[ni][nj], path + [(ni, nj)]))
