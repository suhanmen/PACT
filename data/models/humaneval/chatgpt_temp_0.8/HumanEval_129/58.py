def minPath(grid, k):
    n = len(grid)
    assert n >= 2
    assert k >= 1

    def dfs(x, y, visited, path):
        if len(path) == k:
            return path
        visited.add((x, y))
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        candidates = []
        for i, j in neighbors:
            if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                candidates.append((grid[i][j], i, j))
        if candidates:
            candidates.sort()
            for _, i, j in candidates:
                result = dfs(i, j, visited, path + [grid[i][j]])
                if result:
                    return result
        visited.remove((x, y))
        return None

    # start the DFS from each cell and keep track of the minimum path
    min_path = None
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, set(), [grid[i][j]])
            if path:
                if not min_path or path < min_path:
                    min_path = path

    return min_path
