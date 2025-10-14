# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # calculate total amount of water in the wells
    total_water = sum(sum(row) for row in grid)

    # calculate number of times we need to lower the bucket, rounded up
    num_buckets = math.ceil(total_water / bucket_capacity)

    return num_buckets
