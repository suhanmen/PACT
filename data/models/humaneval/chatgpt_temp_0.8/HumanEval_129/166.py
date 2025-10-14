def minPath(grid, k):
    # Helper function to get the neighbors of a cell
    def get_neighbors(i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if i < len(grid)-1:
            neighbors.append((i+1, j))
        if j < len(grid[0])-1:
            neighbors.append((i, j+1))
        return neighbors
    
    # Helper function to recursively find the minimum path
    def find_min_path(i, j, visited, path):
        visited.add((i, j))
        path.append(grid[i][j])
        if len(path) == k:
            return path
        min_path = None
        for neighbor in get_neighbors(i, j):
            if neighbor not in visited:
                new_path = find_min_path(neighbor[0], neighbor[1], visited.copy(), path.copy())
                if new_path and (not min_path or new_path < min_path):
                    min_path = new_path
        return min_path
    
    # Find the minimum path from every starting cell a
