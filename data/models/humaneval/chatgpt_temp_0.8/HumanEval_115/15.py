# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # count the total number of units of water in the grid
    total_water = sum(sum(row) for row in grid)

    # return 0 if there is no water to extract
    if total_water == 0:
        return 0

    # calculate the number of times we need to lower the bucket
    # to extract all the water, rounding up to the nearest integer
    num_buckets = math.ceil(total_water / bucket_capacity)

    return num_buckets
