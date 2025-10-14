def max_fill(grid, capacity):
    import math
    
    n_wells = len(grid)
    n_units = sum(sum(row) for row in grid)
    n_buckets = math.ceil(n_units / capacity)
    
    return n_buckets
