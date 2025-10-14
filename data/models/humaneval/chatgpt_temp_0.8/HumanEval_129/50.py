def minPath(grid, k):
    n = len(grid)
    if k == 1:
        min_val = min([min(row) for row in grid])
        return [min_val]

    def dfs(curr, path, visited):
        if len(path) == k:
            return path
        visited.add(curr)
        neighbors = [(curr[0]+1, curr[1]), (curr[0]-1, curr[1]), (curr[0], curr[1]+1), (curr[0], curr[1]-1)]
        neighbors = [(r, c) for r, c in neighbors if 0 <= r < n and 0 <= c < n and (r, c) not in visited]
        paths = [dfs(neighbor, path + [grid[neighbor[0]][neighbor[1]]], visited) for neighbor in neighbors]
        return min(paths, key=lambda x: tuple(x))

    min_path = None
    for i in range(n):
        for j in range(n):
            curr = (i, j)
            path = dfs(curr, [grid[i][j]], set())
            if not min_path or path < min_path:
                min_path = path
    return min_path
