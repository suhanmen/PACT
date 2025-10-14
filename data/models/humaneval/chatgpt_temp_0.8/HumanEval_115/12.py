# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # Get the total amount of water in the grid
    total_water = sum(sum(row) for row in grid)

    # Determine how many times the bucket needs to be lowered
    num_buckets = math.ceil(total_water / bucket_capacity)

    return num_buckets
