def max_fill(grid, capacity):
    import math
    
    # Calculate the total water in the grid
    total_water = sum([sum(row) for row in grid])
    
    # Calculate the number of times the buckets need to be lowered
    num_lowers = math.ceil(total_water / capacity)
    
    return num_lowers
