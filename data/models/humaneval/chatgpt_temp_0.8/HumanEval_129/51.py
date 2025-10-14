def minPath(grid, k):
    n = len(grid)
    visited = set()

    def backtrack(curr, path):
        if len(path) == k:
            return path
        if curr in visited:
            return None
        visited.add(curr)
        row, col = curr
        neighbors = []
        if row > 0:
            neighbors.append((row-1, col))
        if row < n-1:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < n-1:
            neighbors.append((row, col+1))
        neighbors.sort(key=lambda x: grid[x[0]][x[1]])
        for neighbor in neighbors:
            result = backtrack(neighbor, path+[grid[neighbor[0]][neighbor[1]]])
            if result:
                return result
        visited.remove(curr)

    start = min(((i, j) for i in range(n) for j in range(n)), key=lambda x: grid[x[0]][x[1]])
    path = [grid[start[0]][start[1]]]
    return backtrack(start, path)
