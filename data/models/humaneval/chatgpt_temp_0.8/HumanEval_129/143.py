def minPath(grid, k):
    n = len(grid)
    visited = set()
    queue = []  # elements in queue are tuples of (path, row, column)
    for i in range(n):
        for j in range(n):
            queue.append(([grid[i][j]], i, j))
    while queue:
        path, row, col = queue.pop(0)
        if len(path) == k:
            return path
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = row + dr, col + dc
            if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                queue.append((path + [grid[r][c]], r, c))
    return None  # no path found
