# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # Determine the total amount of water in the wells
    total_water = sum(sum(row) for row in grid)

    # Determine the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / bucket_capacity)

    return num_buckets
