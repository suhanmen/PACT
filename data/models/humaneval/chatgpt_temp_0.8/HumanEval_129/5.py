def minPath(grid, k):
    n = len(grid)
    visited = set() # set of visited cells
    heap = [] # min-heap of paths, ordered lexicographically
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]] # start from cell (i,j)
            heapq.heappush(heap, (path, i, j))
    while heap: # explore the grid with a breadth-first search
        path, i, j = heapq.heappop(heap)
        if len(path) == k: # found a path of length k
            return path
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # try all neighbors
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                new_path = path + [grid[ni][nj]]
                heapq.heappush(heap, (new_path, ni, nj))
    raise ValueError("No path of length k found")
