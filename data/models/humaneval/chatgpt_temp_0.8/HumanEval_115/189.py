def max_fill(grid, capacity):
    import math
    
    # calculate the total amount of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # calculate the number of times we need to lower the bucket
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
