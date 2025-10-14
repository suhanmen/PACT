# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    num_buckets = 0
    for row in grid:
        num_buckets += math.ceil(sum(row)/bucket_capacity)
    return num_buckets
