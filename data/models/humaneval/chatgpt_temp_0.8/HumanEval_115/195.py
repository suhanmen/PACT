def max_fill(grid, capacity):
    import math

    # calculate the total volume of water in the grid
    total_water = sum(sum(row) for row in grid)

    # calculate the total number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / capacity)

    return num_buckets
