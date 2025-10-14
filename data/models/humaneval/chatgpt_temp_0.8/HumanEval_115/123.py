def max_fill(grid, capacity):
    import math
    
    # Count how many units of water are in each well
    well_water = [sum(row) for row in grid]
    
    # Calculate the total amount of water in all the wells
    total_water = sum(well_water)
    
    # Calculate how many times you need to lower the buckets
    num_times = math.ceil(total_water / capacity)
    
    return num_times
