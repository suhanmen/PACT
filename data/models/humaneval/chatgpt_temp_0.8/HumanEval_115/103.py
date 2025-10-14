# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    num_buckets = 0
    for well in grid:
        num_buckets += math.ceil(sum(well)/bucket_capacity)
    return num_buckets
