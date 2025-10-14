# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    num_buckets = 0
    for row in grid:
        row_sum = sum(row)
        num_buckets += math.ceil(row_sum/bucket_capacity)
    return num_buckets
