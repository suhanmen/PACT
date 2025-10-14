def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], i, j, [grid[i][j]]) for i in range(n) for j in range(n)]
    heapify(heap)

    while heap:
        val, i, j, path = heappop(heap)
        if len(path) == k:
            return path
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                heappush(heap, (grid[ni][nj], ni, nj, path + [grid[ni][nj]]))
