import heapq

def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], (i, j), [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    
    while heap:
        _, (i, j), path = heapq.heappop(heap)
        if len(path) == k:
            return path
        for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                heapq.heappush(heap, (grid[ni][nj], (ni, nj), path + [grid[ni][nj]]))
