def minPath(grid, k):
    n = len(grid)
    visited = set()

    def dfs(x, y, k, path):
        if k == 0:
            return path
        visited.add((x, y))
        min_path = None
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                new_path = dfs(nx, ny, k - 1, path + [grid[nx][ny]])
                if new_path is not None:
                    if min_path is None or new_path < min_path:
                        min_path = new_path
        visited.remove((x, y))
        return min_path

    for i in range(n):
        for j in range(n):
            path = dfs(i, j, k - 1, [grid[i][j]])
            if path is not None:
                return path
