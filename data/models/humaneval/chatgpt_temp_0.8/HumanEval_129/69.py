from heapq import heappop, heappush

def minPath(grid, k):
    n = len(grid)
    heap = [(grid[i][j], (i,j), [grid[i][j]]) for i in range(n) for j in range(n)]
    while heap:
        val, (i,j), path = heappop(heap)
        if len(path) == k: return path
        for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if 0 <= x < n and 0 <= y < n:
                heappush(heap, (grid[x][y], (x,y), path + [grid[x][y]]))
