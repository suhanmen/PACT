def minPath(grid, k):
    n = len(grid)
    visited = set()  # to keep track of visited cells

    def dfs(curr, path):
        if len(path) == k:  # base case
            return path
        visited.add(curr)

        # try all possible neighbors, in lexicographic order
        for i, j in sorted([(curr[0]-1, curr[1]), (curr[0], curr[1]-1), (curr[0], curr[1]+1), (curr[0]+1, curr[1])]):
            if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                res = dfs((i, j), path + [grid[i][j]])
                if res is not None:  # only return a valid path
                    return res

        visited.remove(curr)  # backtrack

    # try starting from each cell, and return the lexicographically smallest path
    return min(dfs((i, j), [grid[i][j]]) for i in range(n) for j in range(n))
