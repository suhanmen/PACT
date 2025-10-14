def minPath(grid, k):
    n = len(grid)
    if n == 0 or n != len(grid[0]) or k <= 0:
        return []
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = [[grid[i][j]]]
    for step in range(2, k + 1):
        for i in range(n):
            for j in range(n):
                path = []
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        for p in dp[ni][nj]:
                            if len(p) == step - 1 and p[-1] < grid[i][j]:
                                path.append([grid[i][j]] + p)
                if len(path) > 0:
                    dp[i][j] = sorted(path)[0:k]
    return sorted(dp, key=lambda x: x[0][0])[0][0]
