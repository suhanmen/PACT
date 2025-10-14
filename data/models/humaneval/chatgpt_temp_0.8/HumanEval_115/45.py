def max_fill(grid, capacity):
    import math
    
    num_buckets = 0
    for well in grid:
        num_buckets += math.ceil(sum(well) / capacity)
        
    return num_buckets
