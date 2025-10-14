def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], [(i, j)]) for i in range(n) for j in range(n)]
    while heap:
        _, path = heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                heappush(heap, (grid[ni][nj], path + [(ni, nj)]))
        visited.add((i, j))
