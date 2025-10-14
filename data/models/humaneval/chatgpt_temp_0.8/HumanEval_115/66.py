def max_fill(grid, capacity):
    import math

    # Determine the total volume of water in the grid
    total_water_volume = sum(sum(row) for row in grid)

    # Determine the number of times we need to lower the buckets
    num_bucket_lowers = math.ceil(total_water_volume / capacity)

    return num_bucket_lowers
