# Define a function to find the minimum path of length k
def minPath(grid, k):
    # Define variables to keep track of the minimum path and the current path
    min_path = float('inf')
    curr_path = []

    # Define a recursive function to explore all possible paths
    def explore_path(i, j, path):
        nonlocal min_path, curr_path

        # If the path length is k, check if it's the minimum path
        if len(path) == k:
            if tuple(path) < tuple(curr_path):
                curr_path = path.copy()
            return

        # If the current path is already longer than the minimum path, return
        if len(path) > min_path:
            return

        # Explore all possible neighboring cells
        for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                explore_path(x, y, path + [grid[x][y]])

    # Explore all possible starting cells
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            explore_path(i, j, [grid[i][j]])

    # Return the minimum
