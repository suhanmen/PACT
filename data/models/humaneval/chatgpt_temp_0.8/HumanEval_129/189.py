def minPath(grid, k):
    n = len(grid)
    def dfs(path):
        if len(path) == k:
            return path
        paths = []
        last = path[-1]
        i, j = last // n, last % n
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= x < n and 0 <= y < n:
                new_pos = x * n + y
                if new_pos not in path:
                    paths.append(dfs(path + [new_pos]))
        return min(paths, key=lambda x: tuple(grid[i // n][i % n] for i in x))
    return dfs([i*n+j for i in range(n) for j in range(n)])
