def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    
    # Define function to get neighbor cells of a given cell
    def get_neighbors(cell):
        row, col = cell
        neighbors = []
        if row > 0:
            neighbors.append((row-1, col))
        if row < len(grid)-1:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < len(grid[0])-1:
            neighbors.append((row, col+1))
        return neighbors
    
    # Define recursive function to find minimum path
    def find_path(cell, path, visited):
        # Add current cell to path and visited set
        path.append(grid[cell[0]][cell[1]])
        visited.add(cell)
        
        # If path is of length k, return it
        if len(path) == k:
            return path
        
        # Find all unvisited neighbor cells
        neighbors = get_neighbors(cell)
        unvisited_neighbors = [n for n in neighbors if n not in visited]
        
        # Recursively find paths from each unvisited neighbo
