def minPath(grid, k):
    def dfs(path, i, j):
        if len(path) == k:
            return path
        min_path = None
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                new_path = dfs(path + [grid[ni][nj]], ni, nj)
                if new_path is not None and (min_path is None or new_path < min_path):
                    min_path = new_path
                visited[ni][nj] = False
        return min_path
    
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            path = dfs([grid[i][j]], i, j)
            if path is not None and (best_path is None or path < best_path):
                best_path = path
            visited[i][j] = False
    return best_path
