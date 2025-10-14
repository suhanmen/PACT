def minPath(grid, k):
    n = len(grid)
    if k == 1:
        return [min([min(row) for row in grid])]
    visited = set()
    heap = [(grid[i][j], [grid[i][j]], i, j) for i in range(n) for j in range(n)]
    heapify(heap)
    while heap:
        path_sum, path, i, j = heappop(heap)
        if len(path) == k:
            return path
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0 <= x < n and 0 <= y < n:
                new_path = path + [grid[x][y]]
                new_sum = sum(new_path)
                heappush(heap, (new_sum, new_path, x, y))
