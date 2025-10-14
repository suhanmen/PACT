def minPath(grid, k):
    n = len(grid)
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(path):
        if len(path) == k:
            return path
        min_path = None
        for i, j in path[-1]:
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    res = dfs(path + [(x, y)])
                    if res is not None:
                        if min_path is None or res < min_path:
                            min_path = res
                    visited.remove((x, y))
        return min_path

    for i in range(n):
        for j in range(n):
            visited.add((i, j))
            res = dfs([(i, j)])
            if res is not None:
                return [grid[i][j]] + [grid[x][y] for x, y in res[1:]]
            visited.remove((i, j))
