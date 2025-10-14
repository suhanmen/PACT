def minPath(grid, k):
    from heapq import heappush, heappop
    N = len(grid)
    heap = []
    for i in range(N):
        for j in range(N):
            heappush(heap, (grid[i][j], [(i, j)]))
    while heap:
        cost, path = heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if i > 0:
            heappush(heap, (cost + 1, path + [(i - 1, j)]))
        if i < N - 1:
            heappush(heap, (cost + 1, path + [(i + 1, j)]))
        if j > 0:
            heappush(heap, (cost + 1, path + [(i, j - 1)]))
        if j < N - 1:
            heappush(heap, (cost + 1, path + [(i, j + 1)]))
