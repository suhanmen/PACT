python
def minPath(grid, k):
    n = len(grid)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = [(grid[i][j], [i, j]) for i in range(n) for j in range(n)]
    heapq.heapify(pq)
    visited = set()
    while pq:
        cost, path = heapq.heappop(pq)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                heapq.heappush(pq, (cost + 1, path + [(ni, nj)]))
