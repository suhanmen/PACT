def max_fill(grid, capacity):
    import math
    
    # calculate the total units of water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # calculate the number of times the bucket needs to be lowered
    num_lowers = math.ceil(total_water / capacity)
    
    return num_lowers
