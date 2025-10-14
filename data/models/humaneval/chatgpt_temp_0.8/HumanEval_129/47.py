def minPath(grid, k):
    def dfs(cell, path):
        if len(path) == k:
            return path
        min_path = None
        for neighbor in get_neighbors(cell):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = dfs(neighbor, path + [grid[neighbor[0]][neighbor[1]]])
                visited.remove(neighbor)
                if min_path is None or new_path < min_path:
                    min_path = new_path
        return min_path
    
    def get_neighbors(cell):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = cell[0] + dr
            c = cell[1] + dc
            if 0 <= r < n and 0 <= c < n:
                neighbors.append((r, c))
        return neighbors
        
    n = len(grid)
    visited = set()
    min_path = None
    for r in range(n):
        for c in range(n):
            visited.clear()
            visited.add((r, c))
            path = dfs((r, c), [grid[r][c]])
            if min_path is
