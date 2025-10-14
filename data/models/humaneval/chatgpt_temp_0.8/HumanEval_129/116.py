def minPath(grid, k):
    n = len(grid)
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(path, i, j):
        if len(path) == k:
            return path
        candidates = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in path:
                candidates.append((grid[ni][nj], ni, nj))
        candidates.sort()
        for val, ni, nj in candidates:
            res = dfs(path + [(ni, nj)], ni, nj)
            if res is not None:
                return [grid[i][j]] + res
        return None

    # Try starting from each cell of the grid
    paths = []
    for i in range(n):
        for j in range(n):
            path = dfs([(i, j)], i, j)
            if path is not None:
                paths.append(path)
    paths.sort()
    return paths[0]
