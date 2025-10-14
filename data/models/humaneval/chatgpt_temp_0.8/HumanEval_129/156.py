def minPath(grid, k):
    n = len(grid)

    # helper function to get neighbors of a cell
    def get_neighbors(i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if i < n-1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < n-1:
            neighbors.append((i, j+1))
        return neighbors

    # helper function to compare two paths
    def compare_paths(path1, path2):
        for i in range(k):
            if path1[i] < path2[i]:
                return -1
            elif path1[i] > path2[i]:
                return 1
        return 0

    # initialize the priority queue with all starting cells
    pq = []
    for i in range(n):
        for j in range(n):
            pq.append((grid[i][j], [(i,j)]))

    # sort the priority queue lexicographically
    pq.sort(key=lambda x: x[0])

    # iterate until we find a path of length k
    while pq:
        _, path = pq.pop(0)
        if len(path) == k:
      
