def max_fill(grid, capacity):
    import math
    # Calculate the total units of water in the grid
    total_water = sum(sum(row) for row in grid)
    # Calculate the number of times the bucket needs to be lowered
    num_buckets = math.ceil(total_water / capacity)
    return num_buckets
