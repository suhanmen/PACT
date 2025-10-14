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

    def backtrack(path, visited):
        """
        A helper function to perform backtracking to find all possible paths of
        length k and keep track of the lexicographically smallest one.
        """
        nonlocal smallest_path, smallest_path_lex
        if len(path) == k:
            if smallest_path is None:
                smallest_path = path
                smallest_path_lex = tuple(path)
            else:
                if tuple(path) < smallest_path_lex:
                    smallest_path = path
                    smallest_path_lex = tuple(path)
            return

        last_val = path[-1]
        for neighbor in neighbors[last_val]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                backtrack(path, visited)
                visited.remove(neighbor)
                path.pop()

    # Define the neighbors of each cell
    neighbors = {}
    n = len(grid)
    for i in range(n):
       
