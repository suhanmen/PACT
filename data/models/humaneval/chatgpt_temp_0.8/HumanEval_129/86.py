def minPath(grid, k):
    n = len(grid)
    if k == 1:
        # Return the smallest cell
        min_cell = min(min(row) for row in grid)
        return [min_cell]
    elif k == n * n:
        # Return the values in the order they appear in the grid
        return [grid[i][j] for i in range(n) for j in range(n)]
    else:
        # Find the minimum path of length k
        visited = set()  # set of visited cells
        path = []  # current path
        min_path = None  # current minimum path
        def dfs(i, j):
            nonlocal visited, path, min_path
            if len(path) == k:
                # We have found a path of length k
                if min_path is None or tuple(path) < tuple(min_path):
                    min_path = list(path)
                return
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                 
