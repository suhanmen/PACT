def minPath(grid, k):
    N = len(grid)
    def dfs(x, y, steps, visited):
        visited.add((x, y))
        if steps == k:
            return [grid[x][y]]
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        candidates = []
        for nx, ny in neighbors:
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                candidates.append(dfs(nx, ny, steps+1, visited.copy()))
        candidates = [c for c in candidates if c is not None]
        if len(candidates) == 0:
            return None
        candidates.sort()
        return [grid[x][y]] + candidates[0]

    paths = []
    for i in range(N):
        for j in range(N):
            path = dfs(i, j, 1, set())
            if path is not None:
                paths.append(path)
    paths.sort()
    return paths[0]
