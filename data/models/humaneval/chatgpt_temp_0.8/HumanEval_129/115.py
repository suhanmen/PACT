def minPath(grid, k):
    # Define a recursive function to find paths of length k starting from a given cell
    def dfs(i, j, path):
        # Base case: if we reached the target length k, return the path
        if len(path) == k:
            return path
        # Recursive case: try all valid neighboring cells and choose the one leading to the lexicographically smallest path of length k
        smallest_path = None
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not visited[ni][nj]:
                visited[ni][nj] = True
                candidate_path = dfs(ni, nj, path + [grid[ni][nj]])
                visited[ni][nj] = False
                if candidate_path is not None and (smallest_path is None or candidate_path < smallest_path):
                    smallest_path = candidate_path
        return smallest_path

    # Try starting the path from every possible cell and choose the lexicographic
