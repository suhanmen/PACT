# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # Count the number of units of water in the grid
    total_water = sum(sum(row) for row in grid)

    # Calculate the number of times we need to lower the buckets
    num_lowers = math.ceil(total_water / bucket_capacity)

    return num_lowers
