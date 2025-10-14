# First, we need a function to find neighbors of a given cell in the grid
def neighbors(grid, i, j):
    """
    Given a grid and a cell (i,j), return a list of its neighboring cells
    """
    n = len(grid)
    if i == 0 and j == 0:
        return [(0,1),(1,0)]
    elif i == 0 and j == n-1:
        return [(0,n-2),(1,n-1)]
    elif i == n-1 and j == 0:
        return [(n-2,0),(n-1,1)]
    elif i == n-1 and j == n-1:
        return [(n-1,n-2),(n-2,n-1)]
    elif i == 0:
        return [(0,j-1),(0,j+1),(1,j)]
    elif i == n-1:
        return [(n-1,j-1),(n-1,j+1),(n-2,j)]
    elif j == 0:
        return [(i-1,0),(i+1,0),(i,1)]
    elif j == n-1:
        return [(i-1,n-1),(i+1,n-1),(i,n-2)]
    else:
        return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

# Now we can implement the main function
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
    lst_A[
