def minPath(grid, k):
    n = len(grid)
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path):
        if len(path) == k:
            return path
        visited.add((i, j))
        next_paths = []
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                next_paths.append(dfs(x, y, path + [grid[x][y]]))
        visited.remove((i, j))
        return min(next_paths)

    min_path = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]])
            if not min_path or path < min_path:
                min_path = path
    return min_path
