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
    
    # First, we need to find the starting point with the smallest value
    start_i, start_j = 0, 0
    min_val = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start_i, start_j = i, j
    
    # We will use Dijkstra's algorithm to find the shortest path
    # Create a dictionary to store the distances to each cell from the starting point
    distances = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
    distances[(start_i, start_j)] = 0

    # Create a set to store the visited cells
    visited = set()

    # Create a priority queue to store the cells to visit next
    pq = [(0, start_i, start_j)]

    # Create a dictionary to store the previous cell in the shortest path
    prev = {}

    while pq:
        # Get the cell with the smallest distance
        dist, i, j = heappop(pq)

        # If we have already visited this cell
