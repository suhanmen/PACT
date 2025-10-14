def minPath(grid, k):
    def dfs(i, j, path):
        if len(path) == k:
            return path
        ans = None
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                ans = min(ans, dfs(ni, nj, path + [grid[ni][nj]]), key=lambda x: x or [])
                visited[ni][nj] = False
        return ans
    n = len(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    ans = None
    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            ans = min(ans, dfs(i, j, [grid[i][j]]), key=lambda x: x or [])
            visited[i][j] = False
    return ans
