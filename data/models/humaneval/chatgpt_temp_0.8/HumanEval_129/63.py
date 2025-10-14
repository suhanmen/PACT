def minPath(grid, k):
    n = len(grid)
    visited = set()

    def dfs(i, j, path):
        if len(path) == k:
            return path

        visited.add((i, j))
        neighbors = []
        if i > 0 and (i-1, j) not in visited:
            neighbors.append((i-1, j))
        if i < n-1 and (i+1, j) not in visited:
            neighbors.append((i+1, j))
        if j > 0 and (i, j-1) not in visited:
            neighbors.append((i, j-1))
        if j < n-1 and (i, j+1) not in visited:
            neighbors.append((i, j+1))

        sorted_neighbors = sorted(neighbors, key=lambda x: grid[x[0]][x[1]])
        for neighbor in sorted_neighbors:
            path.append(grid[neighbor[0]][neighbor[1]])
            res = dfs(neighbor[0], neighbor[1], path)
            if res:
                return res
            path.pop()
            visited.remove(neighbor)

    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            res = dfs(i, j, path)
            if res:
              
