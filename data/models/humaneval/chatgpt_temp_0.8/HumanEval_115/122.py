def max_fill(grid, capacity):
    import math
    
    total_wells = len(grid) * len(grid[0])
    total_water = sum(sum(row) for row in grid)
    
    num_fillings = math.ceil(total_water / capacity)
    
    return num_fillings
