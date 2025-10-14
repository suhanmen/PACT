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
    n = len(grid)
    memo = {} # memoization dictionary to store the computed paths
    
    def dfs(x, y, steps, path):
        """
        Depth-first search function to find the minimum path starting from x,y
        """
        if steps == k: # check if we have visited k cells
            return path
        
        if (x, y, steps) in memo: # check if we have already computed this path
            return memo[(x, y, steps)]
        
        min_path = None # variable to store the minimum path found so far
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # iterate over neighbors
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
                # make sure we don't go off the grid and don't repeat cells
                new_path = dfs(nx, ny, steps + 1, path + [(nx, ny)]) # recursive call
                
                if new_path is not None: # if a path was found
                    if min_pa
