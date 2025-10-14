def max_fill(grid, capacity):
    import math
    
    # Count the total number of water units in the grid
    total_water_units = sum([sum(row) for row in grid])
    
    # Calculate the number of times the bucket needs to be lowered
    num_times_lowered = math.ceil(total_water_units / capacity)
    
    return num_times_lowered
