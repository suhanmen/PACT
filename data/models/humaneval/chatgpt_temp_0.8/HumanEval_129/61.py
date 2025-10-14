def minPath(grid, k):
    n = len(grid)
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, path):
        if len(path) == k:
            return path
        visited.add((x, y))
        next_cells = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                next_cells.append((grid[nx][ny], nx, ny))
        next_cells.sort()
        for cell in next_cells:
            next_path = dfs(cell[1], cell[2], path + [cell[0]])
            if next_path:
                return next_path
        visited.remove((x, y))
        return None

    min_path = None
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]])
            if path:
                if min_path is None or path < min_path:
                    min_path = path
    return min_path
