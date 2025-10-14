def minPath(grid, k):
    n = len(grid)
    if k == 1:
        # if k == 1, return the minimum value in the grid
        return [min(min(row) for row in grid)]
    else:
        # create a 3d array to store the minimum paths of length i ending at (r, c)
        # for i in range(k+1), r in range(n), and c in range(n)
        dp = [[[float('inf')]*(n) for _ in range(n)] for _ in range(k+1)]
        # initialize the base case: the minimum path of length 1 ending at (r, c) is the value in grid[r][c]
        for r in range(n):
            for c in range(n):
                dp[1][r][c] = grid[r][c]
        # for each path length i, starting from 2:
        for i in range(2, k+1):
            # for each cell (r, c):
            for r in range(n):
                for c in range(n):
                    # compute the minimum path of length i ending at (r, c)
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < n and
