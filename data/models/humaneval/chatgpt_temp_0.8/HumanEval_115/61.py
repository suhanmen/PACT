def max_fill(grid, capacity):
    import math
    
    total_water = sum(map(sum, grid))
    bucket_count = math.ceil(total_water / capacity)
    return bucket_count
