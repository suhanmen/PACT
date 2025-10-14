def minPath(grid, k):
    # Start by finding the smallest value on the grid
    smallest_value = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            smallest_value = min(smallest_value, grid[i][j])
    
    # Define a function that returns the lexicographically smallest path of length k
    def dfs(curr, path):
        if len(path) == k:
            return path
        best_path = None
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = curr[0]+di, curr[1]+dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in path and grid[ni][nj] > grid[curr[0]][curr[1]]:
                new_path = dfs((ni, nj), path + [(ni, nj)])
                if new_path is not None and (best_path is None or new_path < best_path):
                    best_path = new_path
        return best_path
    
    # Try all starting positions and return the lexicographically smallest path
    best_path = None
    for i in range(len(grid)):
        fo
