def max_fill(grid, capacity):
    import math
    
    bucket_count = 0
    
    for well in grid:
        water_level = sum(well)
        while water_level > 0:
            water_level -= capacity
            bucket_count += 1
        
        if water_level < 0:
            bucket_count += 1
            
    return bucket_count
