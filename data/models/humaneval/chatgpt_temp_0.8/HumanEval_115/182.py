# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= bucket_capacity <= 10
    """

    # Initialize variables
    total_buckets = 0
    num_wells = len(grid)
    num_units = len(grid[0])

    # Iterate over each well and bucket
    for i in range(num_wells):
        for j in range(num_units):
            # If the current cell contains water, use a bucket to empty it
            if grid[i][j]:
                num_buckets = math.ceil(grid[i][j] / bucket_capacity)
                total_buckets += num_buckets
                # Subtract the amount of water emptied by the bucket from the well
                grid[i][j] -= num_buckets * bucket_capacity

                # If there is water left in the well, move it to the next well
                if j < num_units - 1:
                    grid[i][j + 1] += grid[i][j]
                    grid[i][j] = 0

    return total_buckets
