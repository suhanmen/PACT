python
def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def dfs(x, y, path):
        if len(path) == k:
            return path
        visited[x][y] = True
        min_path = None
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                new_path = dfs(nx, ny, path + [grid[nx][ny]])
                if new_path is not None and (min_path is None or new_path < min_path):
                    min_path = new_path
        visited[x][y] = False
        return min_path

    # start from each cell
    paths = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]])
            if path is not None:
                paths.append(path)
    # find the lexicographically smallest path
    return min(paths)
