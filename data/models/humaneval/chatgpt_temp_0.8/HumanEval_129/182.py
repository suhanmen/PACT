def minPath(grid, k):
    n = len(grid)
    visited = set()
    heap = []  # a min heap of (cost, path) tuples
    for i in range(n):
        for j in range(n):
            start = (grid[i][j], i, j)
            heapq.heappush(heap, (start[0], [start]))
    while heap:
        cost, path = heapq.heappop(heap)
        if len(path) == k:
            return [p[0] for p in path]
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        for nei in neighbors(node, n):
            if nei in visited:
                continue
            new_path = path + [nei]
            heapq.heappush(heap, (get_cost(new_path), new_path))
