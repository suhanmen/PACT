def minPath(grid, k):
    # Define the neighbors of a cell (up, down, left, right)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # Define a recursive function to find the minimum path of length k
    def dfs(r, c, path):
        # Base case: the path has length k, return it
        if len(path) == k:
            return path

        # Recursive case: visit the neighbors and try to extend the path
        res = None
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                # The neighbor is inside the grid, so we can visit it
                new_path = dfs(nr, nc, path + [grid[nr][nc]])
                if new_path is not None:
                    # We found a valid path, check if it's the minimum so far
                    if res is None or new_path < res:
                        res = new_path

        return res

    # Try to start the path from each cell in the grid
    res = None
    for r in range(len(grid)):
