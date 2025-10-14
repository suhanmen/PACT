def minPath(grid, k):
    n = len(grid)

    def dfs(x, y, visited):
        visited.add((x, y))
        if len(visited) == k:
            return [grid[x][y]]
        neighbors = []
        if x > 0 and (x-1, y) not in visited:
            neighbors.append(dfs(x-1, y, visited.copy()))
        if x < n-1 and (x+1, y) not in visited:
            neighbors.append(dfs(x+1, y, visited.copy()))
        if y > 0 and (x, y-1) not in visited:
            neighbors.append(dfs(x, y-1, visited.copy()))
        if y < n-1 and (x, y+1) not in visited:
            neighbors.append(dfs(x, y+1, visited.copy()))
        path = min(neighbors)
        return [grid[x][y]] + path

    paths = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, set())
            if len(path) == k:
                paths.append(path)
    return min(paths)
