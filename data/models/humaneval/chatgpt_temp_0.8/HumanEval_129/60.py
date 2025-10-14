def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(grid[i][j], [(i, j)]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    while heap:
        _, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        x, y = path[-1]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
                new_path = path + [(nx, ny)]
                heapq.heappush(heap, (tuple(grid[i][j] for i, j in new_path), new_path)))
