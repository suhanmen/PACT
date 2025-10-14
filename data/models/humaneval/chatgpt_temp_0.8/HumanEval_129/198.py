def minPath(grid, k):
    # Initialize variables
    n = len(grid)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    # Define function to check if a given path is valid
    def is_valid_path(path):
        for i in range(k - 1):
            if path[i + 1] not in [grid[p[0]][p[1]] for p in neighbors[path[i]]]:
                return False
        return True

    # Define function to get neighbors of a cell
    def get_neighbors(cell):
        neighbors = []
        for move in moves:
            neighbor = (cell[0] + move[0], cell[1] + move[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n:
                neighbors.append(neighbor)
        return neighbors

    # Define function to recursively find minimum path
    def find_min_path(curr_cell, path):
        # Add current cell to path
        path.append(grid[curr_cell[0]][curr_cell[1]])
        # If path is of length k, check if it is valid and return path
        if len(path) == k:
            if is_valid_path(path):
