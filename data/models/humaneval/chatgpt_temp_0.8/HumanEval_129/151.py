def minPath(grid, k):
    n = len(grid)
    start = min((i, j) for i in range(n) for j in range(n))
    paths = [[(start, grid[start[0]][start[1]])]]  # list of (position, value) tuples
    for _ in range(k - 1):
        new_paths = []
        for path in paths:
            curr_pos = path[-1][0]
            for next_pos in [(curr_pos[0] + 1, curr_pos[1]), (curr_pos[0] - 1, curr_pos[1]),
                             (curr_pos[0], curr_pos[1] + 1), (curr_pos[0], curr_pos[1] - 1)]:
                if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
                    next_val = grid[next_pos[0]][next_pos[1]]
                    if next_val not in [p[1] for p in path]:  # ensure no repeated values
                        new_paths.append(path + [(next_pos, next_val)])
        paths = sorted(new_paths, key=lambda p: [x[1] for x in p])[:10]  # keep only top 10 paths
    return [p[i][1] for p in paths for i in range(k)]  # concatenate values of top 10 paths
