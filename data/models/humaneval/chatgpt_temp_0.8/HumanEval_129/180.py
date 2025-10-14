python
def minPath(grid, k):
    n = len(grid)
    all_values = set(range(1, n * n + 1))
    visited = set()
    heap = [(grid[i][j], (i, j), [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        _, (i, j), path = heapq.heappop(heap)
        if len(path) == k:
            return path
        visited.add((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                new_path = path + [grid[ni][nj]]
                if set(new_path) == all_values:
                    heapq.heappush(heap, (grid[ni][nj], (ni, nj), new_path))
    raise ValueError("No path of length k found")
