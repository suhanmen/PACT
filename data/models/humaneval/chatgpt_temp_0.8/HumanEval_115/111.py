def max_fill(grid, capacity):
    import math
    
    # Count the total number of units of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # Calculate the number of buckets needed to empty the wells completely
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
