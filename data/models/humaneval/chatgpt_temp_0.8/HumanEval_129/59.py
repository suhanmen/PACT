def minPath(grid, k):
    n = len(grid)
    # Initialize the visited set and the queue with all cells.
    visited = set()
    queue = [(i, j, [grid[i][j]]) for i in range(n) for j in range(n)]
    # Sort the queue lexicographically by the path so far.
    queue.sort(key=lambda x: x[2])
    # Keep iterating until we find a path of length k.
    while queue:
        x, y, path = queue.pop(0)
        # If we have a path of length k, we're done.
        if len(path) == k:
            return path
        # Mark the current cell as visited.
        visited.add((x, y))
        # Try to add all unvisited neighbor cells to the queue.
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                new_path = path + [grid[nx][ny]]
                # Insert the new path into the sorted queue.
                i = len(queue)
                while i > 0 and new_path < queue[i-1][2]:
                    i 
