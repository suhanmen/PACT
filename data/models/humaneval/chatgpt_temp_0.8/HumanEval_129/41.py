def minPath(grid, k):
    n = len(grid)
    
    def get_neighbors(row, col):
        # Returns a list of tuples representing the valid neighboring cells of (row, col)
        return [(r, c) for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                if 0 <= r < n and 0 <= c < n]

    def dfs(row, col, path):
        # Recursive function that performs a depth-first search on the grid
        # starting from cell (row, col) and adding the visited cells to 'path'
        if len(path) == k:
            return path
        # Add the current cell to the path
        path.append(grid[row][col])
        # Visit all the neighboring cells and choose the lexicographically smallest path
        min_path = None
        for r, c in get_neighbors(row, col):
            if grid[r][c] not in path:
                new_path = dfs(r, c, path[:])
                if new_path is not None and (min_path is None or new_path < min_path):
                    min_path = new_path
        return min_path
    
 
