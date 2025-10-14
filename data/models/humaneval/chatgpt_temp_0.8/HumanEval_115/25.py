def max_fill(grid, capacity):
    import math
    
    # Count the number of units of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # Determine the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
