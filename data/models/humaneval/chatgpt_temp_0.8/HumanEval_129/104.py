def minPath(grid, k):
    n = len(grid)
    if k == 1:
        # if k is 1, return the minimum value in the grid
        return [min(min(row) for row in grid)]
    elif k == 2:
        # if k is 2, return the minimum path of length 2
        # this is simply going from the minimum value to its neighbor
        min_value = min(min(row) for row in grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == min_value:
                    if i > 0:
                        return [min_value, grid[i-1][j]]
                    elif j > 0:
                        return [min_value, grid[i][j-1]]
                    elif i < n-1:
                        return [min_value, grid[i+1][j]]
                    else:
                        return [min_value, grid[i][j+1]]
    else:
        # if k > 2, we use dynamic programming to find the minimum path
        # initialize the DP table with infinite values
        dp = [[float('inf')] * n for _ in range(n)]
        # initialize the s
