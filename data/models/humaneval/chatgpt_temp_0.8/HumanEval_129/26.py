def minPath(grid, k):
    n = len(grid)
    if n == 0:
        return []
    
    # define helper function to get neighbors
    def get_neighbors(i, j):
        res = []
        if i > 0:
            res.append((i-1, j))
        if j > 0:
            res.append((i, j-1))
        if i < n-1:
            res.append((i+1, j))
        if j < n-1:
            res.append((i, j+1))
        return res
    
    # define helper function to compare paths
    def is_smaller_path(path1, path2):
        for i in range(k):
            if path1[i] < path2[i]:
                return True
            elif path1[i] > path2[i]:
                return False
        return False
    
    # define recursive function to find minimum path
    def find_min_path(i, j, steps, path):
        path.append(grid[i][j])
        if steps == k:
            return path
        
        candidates = []
        for ni, nj in get_neighbors(i, j):
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
     
