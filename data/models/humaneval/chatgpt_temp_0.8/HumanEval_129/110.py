def minPath(grid, k):
    n = len(grid)
    min_path = None

    # Define a recursive helper function to explore all possible paths of length k
    def explore_path(path, i, j):
        nonlocal min_path

        # Add the current cell to the path
        path.append(grid[i][j])

        if len(path) == k:
            # If the path has length k, check if it is the new minimum path
            if min_path is None or path < min_path:
                min_path = path.copy()
        else:
            # Otherwise, explore all possible neighbors that have not been visited yet
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in path:
                    explore_path(path, ni, nj)

        # Remove the current cell from the path before returning
        path.pop()

    # Start the exploration from each cell of the grid
    for i in range(n):
        for j in range(n):
            explore_path([], i, 
