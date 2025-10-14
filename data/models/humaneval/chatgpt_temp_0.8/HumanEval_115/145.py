# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # calculate the total water in the wells
    total_water = sum(sum(row) for row in grid)

    # calculate the number of times we need to lower the buckets
    num_buckets = math.ceil(total_water / bucket_capacity)

    return num_buckets
