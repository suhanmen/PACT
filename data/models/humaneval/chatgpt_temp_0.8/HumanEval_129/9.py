def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    paths = {}  # dict of paths, key is (i, j, step), value is path to (i, j) of length step
    heap = []  # min heap of (step, i, j, path)
    for i in range(n):
        for j in range(n):
            heap.append((grid[i][j], i, j, [grid[i][j]]))
    heapq.heapify(heap)
    while heap:
        step, i, j, path = heapq.heappop(heap)
        if len(path) == k:
            return path
        if (i, j, len(path)) not in paths:
            paths[(i, j, len(path))] = path
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    heapq.heappush(heap, (step, ni, nj, path + [grid[ni][nj]]))
    raise ValueError("No path of length k found")
