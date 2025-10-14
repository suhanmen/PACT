def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], i, j, [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while len(visited) < n*n and heap:
        val, i, j, path = heapq.heappop(heap)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if len(path) == k:
            return path
        for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= ni < n and 0 <= nj < n:
                heapq.heappush(heap, (grid[ni][nj], ni, nj, path + [grid[ni][nj]]))
    return None
