def max_fill(grid, capacity):
    import math
    
    # First, we count the total amount of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # Then, we calculate the number of times we need to lower the buckets
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
