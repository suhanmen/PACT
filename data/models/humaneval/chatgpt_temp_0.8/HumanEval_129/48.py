def minPath(grid, k):
    # Define a helper function that returns the neighbors of a cell
    def get_neighbors(i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if i < len(grid)-1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < len(grid[0])-1:
            neighbors.append((i, j+1))
        return neighbors

    # Define a recursive function to find the minimum path of length k
    def find_path(i, j, visited, path):
        # If we have visited k cells, return the path
        if len(visited) == k:
            return path
        # Otherwise, recursively explore all neighbors that have not been visited
        neighbors = get_neighbors(i, j)
        min_path = None
        for ni, nj in neighbors:
            if (ni, nj) not in visited:
                new_visited = visited | {(ni, nj)}
                new_path = path + [grid[ni][nj]]
                candidate_path = find_path(ni, nj, new_visited, 
