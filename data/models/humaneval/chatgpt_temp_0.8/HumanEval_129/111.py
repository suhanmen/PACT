python
def minPath(grid, k):

    n = len(grid)
    start = min(min(row) for row in grid)
    end = max(max(row) for row in grid)
    paths = {}

    def find_path(cell, length, path):
        # base case: we reached the end of the path
        if length == k:
            paths[path] = True
            return

        # explore all neighbors of the current cell
        i, j = cell
        for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= x < n and 0 <= y < n:
                find_path((x,y), length+1, path + [grid[x][y]])

    # start from all possible cells with the smallest value
    for i in range(n):
        for j in range(n):
            if grid[i][j] == start:
                find_path((i,j), 1, [start])

    # return the lexicographically smallest path
    return min(paths.keys())
