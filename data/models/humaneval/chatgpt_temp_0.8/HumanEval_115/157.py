def max_fill(grid, capacity):
    import math
    
    # Calculate the total amount of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # Calculate the number of buckets needed to empty the wells
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
