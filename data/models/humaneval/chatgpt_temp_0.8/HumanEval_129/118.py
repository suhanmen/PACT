def minPath(grid, k):
    n = len(grid)
    q = [(grid[i][j], (i, j), [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(q)
    visited = set()
    while q:
        val, pos, path = heapq.heappop(q)
        if len(path) == k:
            return path
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if i > 0:
            heapq.heappush(q, (grid[i - 1][j], (i - 1, j), path + [grid[i - 1][j]]))
        if j > 0:
            heapq.heappush(q, (grid[i][j - 1], (i, j - 1), path + [grid[i][j - 1]]))
        if i < n - 1:
            heapq.heappush(q, (grid[i + 1][j], (i + 1, j), path + [grid[i + 1][j]]))
        if j < n - 1:
            heapq.heappush(q, (grid[i][j + 1], (i, j + 1), path + [grid[i][j + 1]]))
