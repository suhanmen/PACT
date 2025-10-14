def max_fill(grid, capacity):
    import math
    
    # count the total water units in the grid
    total_water = sum(sum(row) for row in grid)
    
    # calculate the number of times to lower the buckets
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
