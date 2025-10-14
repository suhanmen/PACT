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
    import heapq

    # Define a function to check if a given position is valid
    def is_valid(x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    # Define a function to get the ordered list of values on a given path
    def get_path_values(path):
        return [grid[x][y] for x, y in path]

    # Define a list to store the visited paths, along with their lexicographically
    # smallest path values, and a priority queue (heap) for the unvisited paths
    visited = {}
    queue = []

    # Initialize the queue with all possible paths of length 1 (starting from all cells)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = [(i, j)]
            heapq.heappush(queue, (grid[i][j], path))

    # Loop until we find a path of length k
    while queue:
        # Get the path with the smallest lexicographically smallest value list
        value, path = heapq.heappop(queue)

        # Check if the path has length k
        i
