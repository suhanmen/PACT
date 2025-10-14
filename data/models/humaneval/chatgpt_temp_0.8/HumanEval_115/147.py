def max_fill(grid, capacity):
    import math
    
    # Count the total number of units of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # Calculate the number of times we need to lower the buckets
    num_lowerings = math.ceil(total_water / capacity)
    
    return num_lowerings
