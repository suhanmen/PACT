def max_fill(grid, capacity):
    import math
    
    # finding the total number of units of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # finding the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
