def minPath(grid, k):

    n = len(grid)
    visited = set()
    heap = [(grid[i][j], [grid[i][j]]) for i in range(n) for j in range(n)]

    while heap:
        num, path = heapq.heappop(heap)
        if len(path) == k:
            return path
        i, j = divmod(path[-1] - 1, n)
        for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                heapq.heappush(heap, (grid[ni][nj], path + [grid[ni][nj]]))
