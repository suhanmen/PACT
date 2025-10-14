def max_fill(grid, capacity):
    import math

    # Helper function to check if all wells are empty
    def all_empty(grid):
        for row in grid:
            if sum(row) != 0:
                return False
        return True
    
    # Initialize variables
    count = 0
    n = len(grid)
    m = len(grid[0])
    buckets = [0] * n
    
    # Loop until all wells are empty
    while not all_empty(grid):
        # Calculate how much water to extract from each well
        for i in range(n):
            water = min(capacity, grid[i][buckets[i]])
            grid[i][buckets[i]] -= water
            buckets[i] += 1
            count += water

        # If a well is completely empty, move the bucket to the next well
        for i in range(n):
            if buckets[i] >= m or grid[i][buckets[i]] == 0:
                buckets[i] = 0
    
    return count
