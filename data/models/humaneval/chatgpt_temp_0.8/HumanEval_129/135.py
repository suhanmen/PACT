def minPath(grid, k):
    # Helper function to get the neighbors of a cell
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

    # Helper function to compare two paths
    def compare_paths(path1, path2):
        for i in range(min(len(path1), len(path2))):
            if path1[i] < path2[i]:
                return -1
            elif path1[i] > path2[i]:
                return 1
        if len(path1) < len(path2):
            return -1
        elif len(path1) > len(path2):
            return 1
        else:
            return 0

    # Recursive function to find the minimum path
    def find_path(i, j, visited, length):
        # Base case: we've reached the desired length
        if length == k:
            return [grid[i][j]]
    
