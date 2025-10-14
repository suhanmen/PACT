def minPath(grid, k):
    n = len(grid)

    def dfs(cell, visited, path):
        if len(path) == k:
            return path
        visited.add(cell)
        x, y = cell
        candidates = [(x+dx, y+dy) for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]]
        candidates = [(i, j) for i, j in candidates if 0 <= i < n and 0 <= j < n and (i, j) not in visited]
        candidates = sorted(candidates, key=lambda c: grid[c[0]][c[1]])
        for c in candidates:
            res = dfs(c, visited, path + [grid[c[0]][c[1]]])
            if res:
                return res
        visited.remove(cell)
        return None

    paths = []
    for i in range(n):
        for j in range(n):
            path = dfs((i, j), set(), [grid[i][j]])
            if path:
                paths.append(path)
    return sorted(paths)[0]
