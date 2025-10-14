def max_fill(grid, capacity):
    import math
    
    # Total number of units of water in the grid
    total_units = sum([sum(row) for row in grid])
    
    # Number of times the buckets need to be lowered
    num_buckets = math.ceil(total_units / capacity)
    
    return num_buckets
