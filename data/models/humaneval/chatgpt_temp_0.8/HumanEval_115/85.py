def max_fill(grid, capacity):
    import math
    
    # Count the number of units of water in the grid
    water_units = sum(sum(row) for row in grid)
    
    # Calculate the number of times a bucket of capacity "capacity" can extract water from the grid
    num_buckets = math.ceil(water_units / capacity)
    
    return num_buckets
