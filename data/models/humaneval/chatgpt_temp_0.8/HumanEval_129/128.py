def minPath(grid, k):
    n = len(grid)
    visited = set()
    ans = []

    def dfs(i, j, path):
        if len(path) == k:
            if not ans or path < ans:
                ans[:] = path
            return
        for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= x < n and 0 <= y < n and (x,y) not in visited:
                visited.add((x,y))
                dfs(x, y, path + [grid[x][y]])
                visited.remove((x,y))

    for i in range(n):
        for j in range(n):
            visited.add((i,j))
            dfs(i, j, [grid[i][j]])
            visited.remove((i,j))

    return ans
