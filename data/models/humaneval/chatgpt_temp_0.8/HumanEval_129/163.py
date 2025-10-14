def minPath(grid, k):
    n = len(grid)
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def dfs(x, y, path):
        if len(path) == k:
            return path
        visited.add((x, y))
        next_steps = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                next_steps.append((grid[nx][ny], nx, ny))
        next_steps.sort()
        for val, nx, ny in next_steps:
            res = dfs(nx, ny, path + [val])
            if res:
                return res
        visited.remove((x, y))

    # start from each cell and find the minimum path
    paths = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]])
            if path:
                paths.append(path)

    # find the lexicographically minimum path
    return min(paths)
