def max_fill(grid, capacity):
    import math
    
    # Calculate the total amount of water in the wells
    water_count = sum([sum(row) for row in grid])
    
    # Calculate the number of times we need to lower the bucket
    num_times = math.ceil(water_count / capacity)
    
    return num_times
