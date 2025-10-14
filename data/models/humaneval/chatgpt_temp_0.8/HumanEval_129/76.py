def minPath(grid, k):
    def dfs(cur, path):
        nonlocal ans
        if len(path) == k:
            if path < ans:
                ans = path
            return
        for nxt in adj[cur]:
            dfs(nxt, path + [grid[nxt[0]][nxt[1]]])
    
    n = len(grid)
    adj = [[(i-1,j),(i+1,j),(i,j-1),(i,j+1)] for i in range(n) for j in range(n)]
    ans = [float('inf')] * k
    for i in range(n):
        for j in range(n):
            dfs((i,j), [grid[i][j]])
    return ans
