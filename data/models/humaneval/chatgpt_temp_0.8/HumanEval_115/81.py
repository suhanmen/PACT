def max_fill(grid, capacity):
    import math
    
    # calculate the total amount of water to be extracted
    total_water = sum([sum(row) for row in grid])
    
    # calculate the number of times the bucket needs to be lowered
    num_times_lowered = math.ceil(total_water / capacity)
    
    return num_times_lowered
