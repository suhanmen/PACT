def minPath(grid, k):
    n = len(grid)
    # Use a priority queue to store paths by their lexicographic order
    queue = [(grid[i][j], [(i, j)]) for i in range(n) for j in range(n)]
    heapq.heapify(queue)
    # Keep track of visited cells to avoid cycles
    visited = set()
    while queue:
        # Pop the path with the lowest lexicographic order
        cost, path = heapq.heappop(queue)
        if len(path) == k:
            # Return the values on the visited cells of the path
            return [grid[i][j] for i, j in path]
        # Try to extend the path to neighboring cells
        i, j = path[-1]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                # Add the extended path to the priority queue
                heapq.heappush(queue, (cost + grid[ni][nj], path + [(ni, nj)]))
    # If we haven't found a path of length k, something wen
