def max_fill(grid, capacity):
    import math

    # count the total amount of water in the grid
    total_water = sum(sum(row) for row in grid)

    # calculate the number of times we need to lower the buckets
    num_ops = math.ceil(total_water / capacity)

    return num_ops
