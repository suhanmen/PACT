def minPath(grid, k):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        
        def dfs(curr_i, curr_j, k, path):
            if k == 0:
                return path
            visited[curr_i][curr_j] = True
            res = []
            for di, dj in directions:
                new_i = curr_i + di
                new_j = curr_j + dj
                if 0 <= new_i < n and 0 <= new_j < n and not visited[new_i][new_j]:
                    res.append(dfs(new_i, new_j, k-1, path + [grid[new_i][new_j]]))
            visited[curr_i][curr_j] = False
            return min(res)
        
        # Start the search from each cell in the grid
        min_path = []
        for i in range(n):
            for j in range(n):
                min_path = min(min_path, dfs(i, j, k-1, [grid[i][j]]))
        
        return min_path
