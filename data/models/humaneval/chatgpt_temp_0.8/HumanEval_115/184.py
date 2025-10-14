def max_fill(grid, capacity):
    import math

    # Calculate the total number of units of water in the grid
    total_water = sum([sum(row) for row in grid])

    # Calculate the number of times we need to lower the bucket
    # based on the capacity of the bucket and the total amount of water
    num_buckets = math.ceil(total_water / capacity)

    return num_buckets
