python
from heapq import heappush, heappop

def minPath(grid, k):
    def neighbors(i, j):
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= x < n and 0 <= y < n:
                yield x, y

    n = len(grid)
    q = [(grid[i][j], [(i,j)]) for i in range(n) for j in range(n)]
    while q:
        _, path = heappop(q)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        for x, y in neighbors(i, j):
            if (x, y) not in path:
                heappush(q, (grid[x][y], path + [(x,y)]))
