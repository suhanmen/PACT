def minPath(grid, k):
    N = len(grid)
    visited = set()  # set of visited cells
    heap = [(grid[i][j], [(i, j)]) for i in range(N) for j in range(N)]
    # heap contains pairs (value, path)
    while heap:
        value, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]  # found a path of length k
        i, j = path[-1]
        visited.add((i, j))
        for ni, nj in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                new_path = path + [(ni, nj)]
                heapq.heappush(heap, (value + grid[ni][nj], new_path))
    raise ValueError("No path of length k found")
