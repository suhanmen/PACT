def max_fill(grid, capacity):
    import math
    
    # Calculate the total amount of water in the grid
    total_water = sum([sum(row) for row in grid])
    
    # Calculate the number of times we need to lower the buckets
    num_buckets = math.ceil(total_water/capacity)
    
    # Return the number of times we need to lower the buckets
    return num_buckets
