import heapq

def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[0][0], (0,0), [grid[0][0]])] # value, position, path
    while heap:
        val, (i,j), path = heapq.heappop(heap)
        if len(path) == k:
            return path
        if (i,j) in visited:
            continue
        visited.add((i,j))
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and (ni,nj) not in visited:
                heapq.heappush(heap, (grid[ni][nj], (ni,nj), path+[grid[ni][nj]]))
