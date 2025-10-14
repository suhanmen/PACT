def max_fill(grid, capacity):
    import math
    num_buckets = math.ceil(sum(sum(row) for row in grid) / capacity)
    
    return num_buckets
