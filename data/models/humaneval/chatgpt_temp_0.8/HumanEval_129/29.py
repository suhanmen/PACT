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
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(path, visited):
        """
        Helper function to perform DFS on the grid and return the minimum path.
        """
        nonlocal ans
        
        if len(path) == k:
            # Check if the current path is lexicographically less than the minimum path found so far.
            if not ans or path < ans:
                ans = path[:]
            return
        
        # Get the last element of the current path
        last = path[-1]
        row, col = divmod(last - 1, n)

        # Explore all possible neighbors and continue the search if the neighbor is not already visited.
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] not in visited:
                path.append(grid[new_row][new_col])
                visited.add(grid[new_row][new_col])
                dfs(path, visited)
 
