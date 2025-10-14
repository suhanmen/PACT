def minPath(grid, k):
    n = len(grid)
    if n == 0:
        return []
    m = len(grid[0])
    if m == 0:
        return []
    if k <= 0:
        return []

    def dfs(i, j, visited, path):
        if len(path) == k:
            return path
        visited.add((i, j))
        candidates = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                candidates.append((grid[ni][nj], ni, nj))
        candidates.sort()
        for value, ni, nj in candidates:
            result = dfs(ni, nj, visited, path + [value])
            if result is not None:
                return result
        visited.remove((i, j))
        return None

    for i in range(n):
        for j in range(m):
            result = dfs(i, j, set(), [grid[i][j]])
            if result is not None:
                return result
    return []
