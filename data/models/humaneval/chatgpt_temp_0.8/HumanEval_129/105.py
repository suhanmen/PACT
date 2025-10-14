def minPath(grid, k):
    n = len(grid)
    visited = set()

    def dfs(x, y, path):
        if len(path) == k:
            return path
        visited.add((x, y))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        candidates = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                candidates.append((grid[nx][ny], (nx, ny)))
        candidates.sort()
        for val, (nx, ny) in candidates:
            res = dfs(nx, ny, path + [val])
            if res:
                return res
        visited.remove((x, y))

    for i in range(n):
        for j in range(n):
            res = dfs(i, j, [grid[i][j]])
            if res:
                return res
