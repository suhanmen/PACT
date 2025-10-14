def max_fill(grid, capacity):
    import math
    rows = len(grid)
    cols = len(grid[0])
    total_water = sum(sum(row) for row in grid)
    buckets_needed = math.ceil(total_water / capacity)
    return buckets_needed
