def minPath(grid, k):
    N = len(grid)
    visited = set()
    queue = [(i, j, [grid[i][j]]) for i in range(N) for j in range(N)]
    while queue:
        x, y, path = queue.pop(0)
        if len(path) == k:
            return path
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                new_path = path + [grid[nx][ny]]
                queue.append((nx, ny, new_path))
                queue.sort(key=lambda x: x[2])
    return None
