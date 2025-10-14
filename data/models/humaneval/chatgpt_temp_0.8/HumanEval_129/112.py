def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], i, j, [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        _, i, j, path = heapq.heappop(heap)
        if len(path) == k:
            return path
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                heapq.heappush(heap, (grid[ni][nj], ni, nj, path + [grid[ni][nj]]))
