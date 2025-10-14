def minPath(grid, k):
    n = len(grid)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    def dfs(cell, path):
        if len(path) == k:
            return path

        visited.add(cell)
        next_cells = []
        for dr, dc in neighbors:
            r, c = cell[0] + dr, cell[1] + dc
            if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                next_cells.append((r, c))
        next_cells = sorted(next_cells, key=lambda x: grid[x[0]][x[1]])
        for next_cell in next_cells:
            new_path = dfs(next_cell, path + [grid[next_cell[0]][next_cell[1]]])
            if new_path is not None:
                return new_path
        visited.remove(cell)

    start_cells = [(r, c) for r in range(n) for c in range(n)]
    start_cells = sorted(start_cells, key=lambda x: grid[x[0]][x[1]])
    for start_cell in start_cells:
        path = dfs(start_cell, [grid[start_cell[0]][start_cell[1]]])
        if path is not None:
            return path
