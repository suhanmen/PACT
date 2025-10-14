def max_fill(grid, capacity):
    import math
    
    # calculate the total amount of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # calculate the total number of buckets needed
    total_buckets = math.ceil(total_water / capacity)
    
    # calculate the number of times to lower the buckets
    return total_buckets
