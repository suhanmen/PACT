def max_fill(grid, capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    num_buckets = math.ceil(total_water / capacity)
    return num_buckets
