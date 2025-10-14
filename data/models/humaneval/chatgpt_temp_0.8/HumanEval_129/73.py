def minPath(grid, k):
    n = len(grid)
    visited = set()
    path = []

    def dfs(i, j, steps):
        if steps == k:
            return [grid[i][j]]

        visited.add((i, j))
        neighbors = []

        if i > 0 and (i-1, j) not in visited:
            neighbors.append(dfs(i-1, j, steps+1))
        if i < n-1 and (i+1, j) not in visited:
            neighbors.append(dfs(i+1, j, steps+1))
        if j > 0 and (i, j-1) not in visited:
            neighbors.append(dfs(i, j-1, steps+1))
        if j < n-1 and (i, j+1) not in visited:
            neighbors.append(dfs(i, j+1, steps+1))

        visited.remove((i, j))
        neighbors.sort()
        path.extend(neighbors[0])
        return neighbors[0]

    for i in range(n):
        for j in range(n):
            dfs(i, j, 1)

    return path
