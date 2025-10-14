def minPath(grid, k):
    def neighbors(r, c):
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

    def dfs(r, c, path, k):
        if k == 0:
            return path
        min_path = path + [float('inf')] * k
        for nr, nc in neighbors(r, c):
            new_path = dfs(nr, nc, path + [grid[nr][nc]], k - 1)
            if new_path[-1] < min_path[-1]:
                min_path = new_path
        return min_path

    min_path = [float('inf')] * k
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            path = dfs(r, c, [grid[r][c]], k - 1)
            if path[-1] < min_path[-1]:
                min_path = path
    return min_path