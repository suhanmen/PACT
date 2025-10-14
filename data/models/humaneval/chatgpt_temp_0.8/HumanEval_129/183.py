def minPath(grid, k):
    # Find the starting cell with the smallest value
    min_val = float('inf')
    start_i, start_j = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start_i, start_j = i, j
    
    # Define a recursive function to find the minimum path
    def find_path(i, j, k_left, path):
        # Base case: we have visited k cells
        if k_left == 0:
            return path
        
        # Find the neighbors and sort them by value
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if i < len(grid)-1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < len(grid[i])-1:
            neighbors.append((i, j+1))
        neighbors.sort(key=lambda pos: grid[pos[0]][pos[1]])
        
        # Try each neighbor recursively
        min_path = None
        for ni, nj in neighbors:
    
