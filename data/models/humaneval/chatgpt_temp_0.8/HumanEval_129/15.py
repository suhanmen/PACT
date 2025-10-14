def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    path = []
    min_path = None

    def dfs(i, j, count):
        nonlocal min_path
        if count == k:
            if min_path is None or path < min_path:
                min_path = list(path)
            return
        if i < 0 or i >= n or j < 0 or j >= n or visited[i][j]:
            return
        path.append(grid[i][j])
        visited[i][j] = True
        dfs(i + 1, j, count + 1)
        dfs(i - 1, j, count + 1)
        dfs(i, j + 1, count + 1)
        dfs(i, j - 1, count + 1)
        visited[i][j] = False
        path.pop()

    for i in range(n):
        for j in range(n):
            dfs(i, j, 1)

    return min_path
