def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = [(grid[i][j], [(i, j)]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        _, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                new_path = path + [(ni, nj)]
                heapq.heappush(heap, (grid[ni][nj], new_path))
