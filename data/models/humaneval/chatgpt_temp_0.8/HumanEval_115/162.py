def max_fill(grid, capacity):
    import math
    
    # calculate total amount of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # calculate number of times to lower the buckets
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
