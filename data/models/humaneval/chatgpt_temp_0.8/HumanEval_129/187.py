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
    visited = set()
    heap = [(grid[i][0], [(i, 0)]) for i in range(n)]
    heapq.heapify(heap)
    while heap:
        cost, path = heapq.heappop(heap)
        if len(path) == k:
            return [grid[i][j] for i, j in path]
        i, j = path[-1]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if j < n - 1:
            heapq.heappush(heap, (cost + grid[i][j + 1], path + [(i, j + 1)]))
        if i > 0:
            heapq.heappush(heap, (cost + grid[i - 1][j], path + [(i - 1, j)]))
        if i < n - 1:
            heapq.heappush(heap, (cost + grid[i + 1][j], path + [(i + 1, j)]))
    return []
