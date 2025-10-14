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

    # Create a dictionary to store the coordinates of each value in the grid
    value_to_coord = {}
    for i in range(n):
        for j in range(n):
            value_to_coord[grid[i][j]] = (i, j)

    # Recursive function to find minimum path of length k
    def helper(curr_coord, visited_values):
        # If we have visited k values, return the visited values
        if len(visited_values) == k:
            return visited_values

        # Initialize an empty list to store the minimum path
        min_path = None

        # Check all neighboring cells
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_coord = (curr_coord[0] + neighbor[0], curr_coord[1] + neighbor[1])

            # If the neighboring cell is within the grid and we haven't already visited the value at the cell
            if 0 <= next_coord[0] < n and 0 <= next_coord[1] < n and grid[next_coord[0]][next_coord[1]] not in visited_values:
                # Add the value at 
