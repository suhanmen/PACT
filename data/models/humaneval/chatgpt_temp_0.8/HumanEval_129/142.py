def minPath(grid, k):
    from heapq import heappush, heappop
    N = len(grid)
    visited = set()
    heap = [(grid[i][j], (i, j), [grid[i][j]]) for i in range(N) for j in range(N)]
    
    while heap:
        val, (x, y), path = heappop(heap)
        if len(path) == k:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= i < N and 0 <= j < N and (i, j) not in visited:
                heappush(heap, (grid[i][j], (i, j), path + [grid[i][j]]))
