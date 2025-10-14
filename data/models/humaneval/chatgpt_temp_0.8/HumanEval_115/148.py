def max_fill(grid, capacity):
    import math

    # Find the total amount of water in the grid.
    total_water = sum(sum(row) for row in grid)

    # Calculate the number of buckets required to empty all the wells.
    num_buckets = math.ceil(total_water / capacity)

    return num_buckets
