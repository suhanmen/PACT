def max_fill(grid, capacity):
    import math
    
    # Count the number of units of water in each well
    well_counts = [sum(row) for row in grid]
    
    # Calculate the total number of units of water
    total_count = sum(well_counts)
    
    # Calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_count / capacity)
    
    return num_buckets
