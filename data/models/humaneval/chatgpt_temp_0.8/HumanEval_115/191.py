def max_fill(grid, capacity):
    import math
    
    # calculate the total amount of water in the wells
    total_water = sum([sum(row) for row in grid])
    
    # calculate the number of times the buckets need to be emptied
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
