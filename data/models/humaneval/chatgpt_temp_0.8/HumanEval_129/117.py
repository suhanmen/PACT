def minPath(grid, k):
    N = len(grid)
    visited = set()
    heap = [(grid[i][j], [(i, j)]) for i in range(N) for j in range(N)]
    heapq.heapify(heap)
    while heap:
        cost, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                heapq.heappush(heap, (grid[ni][nj], path + [(ni, nj)]))
