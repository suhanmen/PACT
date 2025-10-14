def max_fill(grid, capacity):
    import math
    
    rows = len(grid)
    cols = len(grid[0])
    
    total_water = 0
    
    for row in grid:
        total_water += sum(row)
    
    buckets_needed = math.ceil(total_water/capacity)
    
    return buckets_needed
