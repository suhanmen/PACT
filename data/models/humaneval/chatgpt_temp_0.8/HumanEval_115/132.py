def max_fill(grid, capacity):
    import math
    
    max_units = 0
    
    for row in grid:
        units = sum(row)
        max_units = max(max_units, units)
    
    return math.ceil(max_units / capacity)
