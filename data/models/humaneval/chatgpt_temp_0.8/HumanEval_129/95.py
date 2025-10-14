import heapq

def minPath(grid, k):
    n = len(grid)
    start = (0, 0)
    end = (n-1, n-1)

    # Helper function to get the neighbors of a cell
    def neighbors(cell):
        r, c = cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                yield (nr, nc)

    # Helper function to compare paths lexicographically
    def path_lt(path1, path2):
        for i in range(k):
            if path1[i] < path2[i]:
                return True
            elif path1[i] > path2[i]:
                return False
        return False

    # Dijkstra's algorithm to find the shortest path of length k
    dist = {cell: float('inf') for cell in [(r, c) for r in range(n) for c in range(n)]}
    dist[start] = 0
    heap = [(0, start, [grid[0][0]])]
    while heap:
        d, cell, path = heapq.heappop(heap)
        if cell == end and len(path) == k:
            return path
        if len(path) > k:
            continue
        if d > dis
